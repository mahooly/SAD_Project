from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *


def index(request):
    return render(request, 'index.html')


def terms(request):
    return render(request, 'terms.html')


def benefactor_registration(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        form = BenefactorRegistraton(request.POST)
        if form.is_valid() and user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.isBen = True
            user.save()
            benefactor = form.save(commit=False)
            benefactor.user = user
            benefactor.save()

        else:
            print(user_form.errors, form.errors)

    else:
        user_form = UserForm()
        form = BenefactorRegistraton()
    return render(request, 'registerBenefactor.html', {'user_form': user_form, 'form': form})


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

        else:
            print(user_form.errors, form.errors)

    else:
        user_form = UserForm()
        form = BenefactorRegistraton()

    return render(request, 'registerOrganization.html', {'user_form': user_form, 'form': form})


def project_creation(request):
    if request.method == 'POST':
        form = ProjectRegistration(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()

        else:
            print(form.errors)

    else:
        form = ProjectRegistration()
    return render(request, 'submitProject.html', {'form': form})


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


def update_benefactor_profile(request):
    if request.method == 'POST':
        user_form = EditUser(request.POST)
        form = EditBenefactorProfile(request.POST)
        if user_form.is_valid() and form.is_valid():
            user = CustomUser.objects.get(username=request.user.username)
            for attr in user_form.data:
                if attr in user_form.fields and user_form.data[attr] is not '':
                    if attr != 'password2':
                        if getattr(user, attr) is not user_form.data[attr]:
                            setattr(user, attr, user_form.data[attr])
            user.save()
            benefactor = Benefactor.objects.get(user=user)
            for attr in form.data:
                if attr in form.fields and form.data[attr] is not '' and form.data[attr] is not 'blank':
                    setattr(benefactor, attr, form.data[attr])
            benefactor.save()
        else:
            print(user_form.errors, form.errors)

    else:
        user_form = UserForm()
        form = EditBenefactorProfile()

    return render(request, 'editProfileBenefactor.html', {'user_form': user_form, 'form': form})


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

    return render(request, 'editProfileOrganization.html', {'user_form': user_form, 'form': form})


def rate(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            new_rate = form.save(commit=False)
            new_rate.user = request.user
            new_rate.save()
        else:
            print(form.errors)

    else:
        form = RateForm()

    return render(request, 'submitProject.html', {'form': form})
