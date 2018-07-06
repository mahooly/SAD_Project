from django.shortcuts import render
from .forms import *


def index(request):
    return render(request, 'index.html')


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
