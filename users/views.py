from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
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
        orgRequirements.append(Requirement.objects.filter(user=orgs[i].user))
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
            organizer.rate = TotalRate.objects.create()
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
            if user.state == 1:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # disabled account
                return
        else:
            # invalid login
            return
    else:
        return render(request, 'login.html')


# updated fields
# permission
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
            for attr in user_form.data:
                if attr in user_form.fields and user_form.data[attr] != '':
                    if attr != 'password2':
                        if getattr(user, attr) is not user_form.data[attr]:
                            if attr == 'password':
                                user.set_password(user_form.data[attr])
                            else:
                                setattr(user, attr, user_form.data[attr])

            if 'image' in request.FILES:
                user.image = request.FILES['image']

            user.save()
            benefactor = Benefactor.objects.get(user=user)
            for attr in form.data:
                if attr in form.fields and form.data[attr] != '' and form.data[attr] != 'blank':
                    setattr(benefactor, attr, form.data[attr])
            benefactor.save()

            for a in abilities:
                name = a.name
                if request.POST.get(name) is not None:
                    try:
                        UserAbilities.objects.get(abilityId=a, username=user)
                    except ObjectDoesNotExist:
                        UserAbilities.objects.create(abilityId=a, username=user)
                else:
                    try:
                        usab = UserAbilities.objects.get(abilityId=a, username=user)
                        usab.delete()
                    except ObjectDoesNotExist:
                        pass

            for attr in week_form.data:
                if attr in week_form.fields and getattr(week, attr) != week_form.data[attr]:
                    setattr(week, attr, week_form.data[attr])
            week.save()

            Report.objects.create(benefactor=user, type='4', operator='3', date=datetime.datetime.today(),
                                  time=datetime.datetime.now())

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


# permission
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
                            if attr == 'password':
                                user.set_password(user_form.data[attr])
                            else:
                                setattr(user, attr, user_form.data[attr])

            if 'image' in request.FILES:
                user.image = request.FILES['image']

            user.save()
            organization = Organizer.objects.get(user=user)
            for attr in form.data:
                if attr in form.fields and form.data[attr] is not '' and form.data[attr] is not 'blank':
                    setattr(organization, attr, form.data[attr])
                organization.save()

            Report.objects.create(organization=user, type='4', operator='4', date=datetime.datetime.today(),
                                  time=datetime.datetime.now())
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
# permission
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
    name = request.POST.get('org', '')
    all_req = Requirement.objects.filter(user__organizer__name__icontains=name)
    all_ab = Ability.objects.all()
    req_ab = []

    if request.method == 'POST':
        sort_type = request.POST['sortType']

        if sort_type == "rateD":
            all_req = all_req.order_by('user__organizer__rate__totalRate')

        if sort_type == "rateA":
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
            all_req = all_req.filter(
                user__organizer__rate__totalRate__gte=int(request.POST.get('minimumtotalrating', 0)))
        except ValueError:
            all_req = all_req.filter(user__organizer__rate__totalRate__gte=0)

        ability = request.POST['field']
        if ability != "blank":
            temp_reqs = []
            for req in all_req:
                if len(RequirementAbilities.objects.filter(reqId=req.id, abilityId=ability)):
                    temp_reqs.append(req)

            all_req = temp_reqs

    for req in all_req:
        result = RequirementAbilities.objects.filter(reqId=req.id)
        if len(result) != 0:
            req_ab.append(result)

    return render(request, 'searchRequirement.html', {'abilities': all_ab, 'reqAbilities': req_ab})


def list_abilities(request):
    name = request.POST.get('field', '')
    if name == 'blank':
        name = ''

    all_abilities = Ability.objects.filter(name__icontains=name)
    all_useres = CustomUser.objects.all()
    all_user_abilities = UserAbilities.objects.all()
    user_abilities = []

    if request.method == 'POST':

        for us in all_useres:
            result = all_user_abilities.filter(abilityId=us.id)
            if len(result) != 0:
                user_abilities.append(result)

    # print("allAb")
    # print(all_abilities)
    # print("userAb")
    # print(user_abilities)

    return render(request, 'searchAbilities.html', {'abilities': all_abilities, 'userAbilities:': user_abilities})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username, state=True)
    if user.isBen:
        if request.user.username == username:
            benefactor = Benefactor.objects.get(user=user)
            week = WeeklySchedule.objects.get(id=benefactor.wId.id)
            user_abilities = UserAbilities.objects.filter(username=user.username)
            return render(request, 'personalProfileBenefactor.html',
                          {'user': user, 'benefactor': benefactor, 'week': week, 'user_abilities': user_abilities})
        else:
            benefactor = Benefactor.objects.get(user=user)
            week = WeeklySchedule.objects.get(id=benefactor.wId.id)
            user_abilities = UserAbilities.objects.filter(username=user.username)
            return render(request, 'benefactorsProfileView.html',
                          {'user': user, 'benefactor': benefactor, 'week': week, 'user_abilities': user_abilities,
                           'rangee': range(28)})
    elif user.isOrg:
        if request.user.username == username:
            organization = Organizer.objects.get(user=user)
            projects = Project.objects.filter(user=user)
            requirements = Requirement.objects.filter(user=user)
            reqability = []
            for req in requirements:
                reqability.append(RequirementAbilities.objects.filter(reqId=req))
            return render(request, 'personalProfileOrganization.html',
                          {'user': user, 'org': organization, 'projects': projects, 'requirements': requirements,
                           'reqability': reqability, 'rangee': range(28)})
        else:
            user = get_object_or_404(CustomUser, username=username)
            organization = Organizer.objects.get(user=user)
            projects = Project.objects.filter(user=user)
            requirements = Requirement.objects.filter(user=user)
            reqability = []
            for req in requirements:
                reqability.append(RequirementAbilities.objects.filter(reqId=req))
            return render(request, 'organizationProfileView.html',
                          {'user': user, 'org': organization, 'projects': projects, 'requirements': requirements,
                           'reqability': reqability, 'rangee': range(28)})


@login_required
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
                                  date=datetime.datetime.today(), time=datetime.datetime.now(), payment=0)
        else:
            totalRate = TotalRate.objects.get(id=user.organizer.rate.id)
            Report.objects.create(benefactor=request.user, organization=user, type='1', operator='1', rateId=rate,
                                  date=datetime.datetime.today(), time=datetime.datetime.now(), payment=0)

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


# permission
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


# permission
@login_required
def waiting_registers(request):
    if request.method == 'POST':
        split = request.POST['req'].split('-')
        user = CustomUser.objects.get(id=split[0])
        if split[1] == '1':
            user.state = True
            send_mail('تایید حساب کاربری', 'حساب کاربری شما تایید شده است!', 'sender@mehraneh.com', [user.email])
        else:
            user.state = False
        user.save()
    users = CustomUser.objects.filter(state=None)
    return render(request, 'waitingRegisters.html', {'users': users})


# TODO add search abilities, report, waiting requests, forget password


def send_request_organization(request, username, reqId):
    if request.method == 'POST':
        user = CustomUser.objects.get(username=username)
        requirement = Requirement.objects.get(id=reqId)
        desc = request.POST['description']
        if requirement.typeOfCooperation != 'atHome':
            weekForm = WeekForm(request.POST)
            week = weekForm.save()
            week.save()
            Request.objects.create(benefactorId=request.user, organizationId=user, wId=week, city=requirement.city,
                                   description=desc)
        else:
            Request.objects.create(benefactorId=request.user, organizationId=user, isAtHome=True, city=requirement.city,
                                   description=desc)

        send_mail('پیشنهاد جدید', 'شما یک پیشنهاد جدید از طرف فلانی دارید', 'sender@mehraneh.com', [user.email])
        Report.objects.create(benefactor=request.user, organization=user, type='2', description=desc, operator='1',
                              date=datetime.datetime.today(), time=datetime.datetime.now())
        return render(request, 'thanks.html')


def report_admin(request):
    reports = Report.objects.all()
    return render(request, 'reportForAdmin.html', {'reports': reports})


def send_request_benefactor(request, username):
    if request.method == 'POST':
        print(request.POST)
        user = CustomUser.objects.get(username=username)
        abilities = Ability.objects.all()
        desc = request.POST['description']
        if user.benefactor.typeOfCooperation != 'atHome':
            weekForm = WeekForm(request.POST)
            week = weekForm.save()
            week.save()
            req = Request.objects.create(benefactorId=user, organizationId=request.user, wId=week, whoSubmit='2', city=user.benefactor.city, description=desc)
        else:
            req = Request.objects.create(benefactorId=user, organizationId=request.user, isAtHome=True, whoSubmit='2',
                                   city=user.benefactor.city, description=desc)
        for a in abilities:
            name = a.name
            if request.POST.get(name) is not None:
               RequestAbilities.objects.create(reqId=req, abilityId=a)
        send_mail('پیشنهاد جدید', 'شما یک پیشنهاد جدید از طرف فلانی دارید', 'sender@mehraneh.com', [user.email])
        Report.objects.create(benefactor=request.user, organization=user, type='2', description=desc, operator='2',
                              date=datetime.datetime.today(), time=datetime.datetime.now())
        return render(request, 'thanks.html')


