from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import *


#TODO fix display ben, org
def index(request):
    orgs = Organizer.objects.all()[:4]
    bens = Benefactor.objects.all()[:4]
    return render(request, 'index.html', {'bens': bens, 'orgs': orgs})


def terms(request):
    return render(request, 'terms.html')


#TODO add total rate
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
            benefactor = form.save(commit=False)
            benefactor.user = user
            benefactor.wId = week
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


#TODO add missing fields, front
def organization_registration(request):
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
            organizer.save()

            return render(request, 'thanks.html')

        else:
            print(user_form.errors, form.errors)

    else:
        user_form = UserForm()
        form = BenefactorRegistraton()
    cities = City.objects.all()
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

            print(request.POST)
            for c in categories:
                name = c.name
                if request.POST.get(name) is not None:
                    CategoryProject.objects.create(categoryId=c, projectId=project)

        else:
            print(form.errors)

    else:
        form = ProjectRegistration()
    return render(request, 'submitProject.html', {'form': form, 'categories': categories, 'cities': cities})


#TODO add invalid
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

            Report.objects.create(benefactor=user, type='4', operator='3', update=update, date=datetime.datetime.today(), time=datetime.datetime.now())

        else:
            print(user_form.errors, form.errors, week_form.errors)

    else:
        user_form = UserForm()
        form = EditBenefactorProfile()
        week_form = WeekForm()

    return render(request, 'editProfileBenefactor.html',
                  {'user_form': user_form, 'form': form, 'week_form': week_form, 'abilities': abilities, 'user': user,
                   'person': benefactor, 'week': week, 'user_abilities': user_abilities, 'rangee': range(28)})


#TODO add missing fields, report object
@login_required
def update_organization_profile(request):
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
            user.save()
            organization = Organizer.objects.get(user=user)
            for attr in form.data:
                if attr in form.fields and form.data[attr] is not '' and form.data[attr] is not 'blank':
                    setattr(organization, attr, form.data[attr])
                organization.save()
        else:
            print(user_form.errors, form.errors)

    else:
        user_form = UserForm()
        form = EditBenefactorProfile()

    user = CustomUser.objects.get(username=request.user.username)
    organization = user.organizer

    return render(request, 'editProfileOrganization.html', {'user_form': user_form, 'form': form, 'user': user, 'org': organization})


#TODO filter and front
def list_projects(request):
    if request.method == 'POST':
        name = request.POST['org']
        projects = Project.objects.filter(user__organizer__name=name)
        return render(request, 'searchProject.html', {'projects': projects})
    else:
        return render(request, 'searchProject.html')


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
    return render(request, 'organizationProfileView.html', {'user': user, 'org': organization, 'projects': projects, 'requirements': requirements})


#TODO add links
def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    if user.isBen:
        benefactor = Benefactor.objects.get(user=user)
        week = WeeklySchedule.objects.get(id=benefactor.wId.id)
        user_abilities = UserAbilities.objects.filter(username=user.username)
        return render(request, 'personalProfileBenefactor.html', {'user': user, 'benefactor': benefactor, 'week': week, 'user_abilities': user_abilities})
    elif user.isOrg:
        organization = Organizer.objects.get(user=user)
        return render(request, 'personalProfileOrganization.html', {'user': user, 'organization': organization})


#TODO report object, submit
def comment(request, username):
    user = get_object_or_404(CustomUser, username=username)
    if request.method == 'POST':
        print(request.data)

    else:
        if user.isBen:
            benefactor = Benefactor.objects.get(user=user)
            return render(request, 'comment.html', {'user': user, 'benefactor': benefactor})
        else:
            organization = Organizer.objects.get(user=user)
            return render(request, 'comment.html', {'user': user, 'organization': organization})


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

    return render(request, 'submitRequirement.html', {'form': form, 'week_form': week_form, 'abilities': abilities, 'rangee': range(28), 'cities': cities})


#TODO add search requirements, abilities, report, waiting requests, registers, forget password