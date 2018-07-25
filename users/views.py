from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import *


def index(request):
    orgs = Organizer.objects.all()[:4]
    bens = Benefactor.objects.all()[:4]
    orgRequirements = []
    orgProjects = []
    benAbilities = []
    ratingOrg = []
    ratingBens = []
    for i in range(4):
        orgProjects.append(Project.objects.filter(user=orgs[i].user))
        benAbilities.append(UserAbilities.objects.filter(username=bens[i].user))
        ratingOrg.append(TotalRate.objects.get(id=orgs[i].rate.id))
        ratingBens.append(TotalRate.objects.get(id=bens[i].rate.id))
        # orgRequirements.append(Requirement.objects.filter(user=orgs[i].user))
    for r in ratingBens:
        print(r.totalRate)
    return render(request, 'index.html',
                  {'bens': bens, 'orgs': orgs, 'orgProjects': orgProjects, 'benAbilities': benAbilities,
                   'ratingOrg': ratingOrg, 'ratingBens': ratingBens, 'orgRequirements': orgRequirements})


def terms(request):
    return render(request, 'terms.html')


def benefactor_registration(request):
    abilities = Ability.objects.all()
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        form = BenefactorRegistraton(request.POST)
        week_form = WeekForm(request.POST)
        if form.is_valid() and user_form.is_valid() and week_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.isBen = True
            user.save()
            week = week_form.save()
            week.save()
            rate = TotalRate.objects.create()
            benefactor = form.save(commit=False)
            benefactor.user = user
            benefactor.wId = week
            benefactor.rate = rate
            benefactor.save()

            for a in abilities:
                name = a.name
                if request.POST.get(name) is not None:
                    UserAbilities.objects.create(abilityId=a, username=user)

            return render(request, 'thanks.html')

        else:
            print(user_form.errors, form.errors)

    else:
        user_form = UserForm()
        form = BenefactorRegistraton()
        week_form = WeekForm()
    cities = City.objects.all()
    return render(request, 'registerBenefactor.html',
                  {'user_form': user_form, 'form': form, 'week_form': week_form, 'abilities': abilities,
                   'rangee': range(28), 'cities': cities})


# TODO add missing fields, front
def organization_registration(request):
    cities = City.objects.all()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        form = OrganizationRegistration(request.POST, request.FILES)

        if user_form.is_valid() and form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.isOrg = True
            user.save()
            organizer = form.save(commit=False)
            organizer.user = user
            organizer.rate= TotalRate.objects.create()
            organizer.save()

            return render(request, 'thanks.html')

        else:
            print(user_form.errors, form.errors)

    else:
        user_form = UserForm()
        form = BenefactorRegistraton()

    return render(request, 'registerOrganization.html', {'user_form': user_form, 'form': form, 'cities': cities})


@login_required
def project_creation(request):
    categories = Category.objects.all()
    cities = City.objects.all()
    if request.method == 'POST':
        form = ProjectRegistration(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()

            for c in categories:
                name = c.name
                if request.POST.get(name) is not None:
                    CategoryProject.objects.create(categoryId=c, projectId=project)

        else:
            print(form.errors)

    else:
        form = ProjectRegistration()
    return render(request, 'submitProject.html', {'form': form, 'categories': categories, 'cities': cities})


# TODO add invalid
def mylogin(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.isBen:
                    return HttpResponseRedirect('/')
                elif user.isOrg:
                    return HttpResponseRedirect('/')
            else:
                # disabled account
                return
        else:
            # invalid login
            return
    else:
        return render(request, 'login.html')


@login_required
def update_benefactor_profile(request):
    abilities = Ability.objects.all()
    user = CustomUser.objects.get(username=request.user.username)
    benefactor = user.benefactor
    cities = City.objects.all()
    week = WeeklySchedule.objects.get(id=benefactor.wId.id)
    user_abilities = UserAbilities.objects.filter(username=user.username)
    if request.method == 'POST':
        user_form = EditUser(request.POST, request.FILES)
        form = EditBenefactorProfile(request.POST)
        week_form = WeekForm(request.POST)
        if user_form.is_valid() and form.is_valid() and week_form.is_valid():
            update = BenefactorUpdatedFields.objects.create(benefactor=user)

            for attr in user_form.data:
                if attr in user_form.fields and user_form.data[attr] != '':
                    if attr != 'password2':
                        if getattr(user, attr) is not user_form.data[attr]:
                            setattr(user, attr, user_form.data[attr])
                            setattr(update, attr, True)

            if 'image' in request.FILES:
                user.image = request.FILES['image']
                update.image = True

            user.save()
            benefactor = Benefactor.objects.get(user=user)
            for attr in form.data:
                if attr in form.fields and form.data[attr] != '' and form.data[attr] != 'blank':
                    setattr(benefactor, attr, form.data[attr])
                    setattr(update, attr, True)
            benefactor.save()

            for a in abilities:
                name = a.name
                if request.POST.get(name) is not None:
                    try:
                        UserAbilities.objects.get(abilityId=a, username=user)
                    except ObjectDoesNotExist:
                        UserAbilities.objects.create(abilityId=a, username=user)
                        update.ability = True
                else:
                    try:
                        usab = UserAbilities.objects.get(abilityId=a, username=user)
                        usab.delete()
                        update.ability = True
                    except ObjectDoesNotExist:
                        pass

            for attr in week_form.data:
                if attr in week_form.fields and getattr(week, attr) != week_form.data[attr]:
                    setattr(week, attr, week_form.data[attr])
                    update.week = True
            week.save()

            update.save()

            Report.objects.create(benefactor=user, type='4', operator='3', update=update,
                                  date=datetime.datetime.today(), time=datetime.datetime.now())

        else:
            print(user_form.errors, form.errors, week_form.errors)

    else:
        user_form = UserForm()
        form = EditBenefactorProfile()
        week_form = WeekForm()

    return render(request, 'editProfileBenefactor.html',
                  {'user_form': user_form, 'form': form, 'week_form': week_form, 'abilities': abilities, 'user': user,
                   'person': benefactor, 'week': week, 'user_abilities': user_abilities, 'rangee': range(28),
                   'cities': cities})


# TODO add missing fields, report object
@login_required
def update_organization_profile(request):
    cities = City.objects.all()
    if request.method == 'POST':
        user_form = EditUser(request.POST)
        form = EditOrganizationProfile(request.POST)
        if user_form.is_valid() and form.is_valid():
            user = CustomUser.objects.get(username=request.user.username)
            for attr in user_form.data:
                if attr in user_form.fields and user_form.data[attr] is not '':
                    if attr != 'password2':
                        if getattr(user, attr) is not user_form.data[attr]:
                            setattr(user, attr, user_form.data[attr])

            if 'image' in request.FILES:
                user.image = request.FILES['image']
                # update.image = True

            user.save()
            organization = Organizer.objects.get(user=user)
            for attr in form.data:
                if attr in form.fields and form.data[attr] is not '' and form.data[attr] is not 'blank':
                    setattr(organization, attr, form.data[attr])
                organization.save()

                # Report.objects.create(organization=user, type='4', operator='4', update=update,
                # date=datetime.datetime.today(), time=datetime.datetime.now())
        else:
            print(user_form.errors, form.errors)

    else:
        user_form = UserForm()
        form = EditBenefactorProfile()

    user = CustomUser.objects.get(username=request.user.username)
    organization = user.organizer

    return render(request, 'editProfileOrganization.html', {'user_form': user_form, 'form': form, 'user': user,
                                                            'org': organization, 'cities': cities})


# TODO filter
def list_projects(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['org']
        sortType = request.POST['sortType']
        projects = Project.objects.filter(user__organizer__name__icontains=name)
        if sortType == "alreadyD":
            projects = projects.order_by('-alreadyPaid')
        if sortType == "alreadyA":
            projects = projects.order_by('alreadyPaid')
        if sortType == "budgetD":
            projects = projects.order_by('-budget')
        if sortType == "budgetA":
            projects = projects.order_by('budget')
        return render(request, 'searchProject.html', {'projects': projects, 'categories': categories})
    else:
        projects = Project.objects.all()
        return render(request, 'searchProject.html', {'projects': projects, 'categories': categories})


def list_requirement(request):
    name= request.POST.get('org','')
    all_req =Requirement.objects.filter(user__organizer__name__icontains=name)
    all_ab = Ability.objects.all()
    req_ab = []

    if request.method == 'POST':
        sort_type = request.POST['sortType']

        if sort_type == "rateD":
            all_req=all_req.order_by('user__organizer__rate__totalRate')

        if sort_type=="rateA":
            all_req = all_req.order_by('-user__organizer__rate__totalRate')

        if sort_type == "participantsA":
            all_req = all_req.order_by('-NOP')

        if sort_type == "participantsD":
            all_req = all_req.order_by('NOP')


        try:
            all_req = all_req.filter(NOP__gte=int(request.POST.get('minimumNOP')))
        except ValueError:
            all_req = all_req.filter(NOP__gte=0)

        try:
            all_req = all_req.filter(user__organizer__rate__totalRate__gte=int(request.POST.get('minimumtotalrating',0)))
        except ValueError:
            all_req = all_req.filter(user__organizer__rate__totalRate__gte=0)

    for req in all_req:
        result = RequirementAbilities.objects.filter(reqId=req.id)
        if len(result) !=0:
            req_ab.append(result)


    return render(request, 'searchRequirement.html', {'abilities': all_ab, 'reqAbilities': req_ab})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_profile_benefactor(request, username):
    user = get_object_or_404(CustomUser, username=username)
    benefactor = Benefactor.objects.get(user=user)
    week = WeeklySchedule.objects.get(id=benefactor.wId.id)
    user_abilities = UserAbilities.objects.filter(username=user.username)
    return render(request, 'benefactorsProfileView.html',
                  {'user': user, 'benefactor': benefactor, 'week': week, 'user_abilities': user_abilities,
                   'rangee': range(28)})


def user_profile_organization(request, username):
    user = get_object_or_404(CustomUser, username=username)
    organization = Organizer.objects.get(user=user)
    projects = Project.objects.filter(user=user)
    requirements = Requirement.objects.filter(user=user)
    return render(request, 'organizationProfileView.html',
                  {'user': user, 'org': organization, 'projects': projects, 'requirements': requirements})


# TODO add links
def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    if user.isBen:
        benefactor = Benefactor.objects.get(user=user)
        week = WeeklySchedule.objects.get(id=benefactor.wId.id)
        user_abilities = UserAbilities.objects.filter(username=user.username)
        return render(request, 'personalProfileBenefactor.html',
                      {'user': user, 'benefactor': benefactor, 'week': week, 'user_abilities': user_abilities})
    elif user.isOrg:
        organization = Organizer.objects.get(user=user)
        return render(request, 'personalProfileOrganization.html', {'user': user, 'organization': organization})


def rate_user(request, username):
    user = get_object_or_404(CustomUser, username=username)
    if request.method == 'POST':
        form = RateForm(request.POST)
        rate = form.save(commit=False)
        rate.user = request.user
        rate.ratedUser = user
        rate.save()
        if user.isBen:
            totalRate = TotalRate.objects.get(id=user.benefactor.rate.id)
            Report.objects.create(benefactor=user, organization=request.user, type='1', operator='2', rateId=rate,
                                  date=datetime.datetime.today(), time=datetime.datetime.now())
        else:
            totalRate = TotalRate.objects.get(id=user.organizer.rate.id)
            Report.objects.create(benefactor=request.user, organization=user, type='1', operator='1', rateId=rate,
                                  date=datetime.datetime.today(), time=datetime.datetime.now())

        count = Rate.objects.filter(ratedUser=user).count()
        totalRate.f1 = ((totalRate.f1 * (count - 1)) + ((rate.f1 - 1) / 4 * 100)) / count
        totalRate.f2 = ((totalRate.f2 * (count - 1)) + ((rate.f2 - 1) / 4 * 100)) / count
        totalRate.f3 = ((totalRate.f3 * (count - 1)) + ((rate.f3 - 1) / 4 * 100)) / count
        totalRate.f4 = ((totalRate.f4 * (count - 1)) + ((rate.f4 - 1) / 4 * 100)) / count
        totalRate.f5 = ((totalRate.f5 * (count - 1)) + ((rate.f5 - 1) / 4 * 100)) / count
        totalRate.totalRate = round((totalRate.totalRate * (count - 1) + (
                (rate.f1 - 1) / 4 + (rate.f2 - 1) / 4 + (rate.f3 - 1) / 4 + (rate.f4 - 1) / 4 + (
                rate.f5 - 1) / 4) / 5 * 100) / count, 1)
        totalRate.save()
        return render(request, 'thanks.html')

    else:
        form = RateForm()
        if user.isBen:
            benefactor = Benefactor.objects.get(user=user)
            return render(request, 'comment.html', {'user': user, 'benefactor': benefactor, 'form': form})
        else:
            organization = Organizer.objects.get(user=user)
            return render(request, 'comment.html', {'user': user, 'organization': organization, 'form': form})


def project(request, username, pId):
    user = get_object_or_404(CustomUser, username=username)
    organization = Organizer.objects.get(user=user)
    proj = get_object_or_404(Project, id=pId)
    return render(request, 'project.html', {'user': user, 'org': organization, 'project': proj})


@login_required
def submit_requirement(request):
    abilities = Ability.objects.all()
    cities = City.objects.all()
    if request.method == 'POST':
        form = RequirementForm(request.POST)
        week_form = WeekForm(request.POST)
        if form.is_valid() and week_form.is_valid():
            week = week_form.save()
            week.save()
            requirement = form.save(commit=False)
            requirement.user = request.user
            requirement.wId = week
            requirement.NOP = 0
            requirement.save()

            for a in abilities:
                name = a.name
                if request.POST.get(name) is not None:
                    RequirementAbilities.objects.create(abilityId=a, reqId=requirement)

        else:
            print(form.errors, week_form.errors)
    else:
        form = RequirementForm()
        week_form = WeekForm()

    return render(request, 'submitRequirement.html',
                  {'form': form, 'week_form': week_form, 'abilities': abilities, 'rangee': range(28), 'cities': cities})

    # TODO add search requirements, abilities, report, waiting requests, registers, forget password
