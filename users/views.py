from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import *


def admin_only(login_url='404'):
    return user_passes_test(lambda u: (not u.isBen and not u.isOrg), login_url=login_url)


def benefactor_only(login_url='404'):
    return user_passes_test(lambda u: u.isBen, login_url=login_url)


def organization_only(login_url='404'):
    return user_passes_test(lambda u: u.isOrg, login_url=login_url)


def admin_org(login_url='404'):
    return user_passes_test(lambda u: (u.isOrg or (not u.isBen and not u.isBen)), login_url=login_url)


def admin_ben(login_url='404'):
    return user_passes_test(lambda u: (u.isBen or (not u.isBen and not u.isBen)), login_url=login_url)


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


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
            rate = TotalRate.objects.create()
            benefactor = form.save(commit=False)
            benefactor.user = user
            if benefactor.typeOfCooperation != 'atHome':
                week = week_form.save()
                week.save()
            else:
                week = None
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
@organization_only
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

            return render(request, 'thanksSubmitProject.html')

        else:
            print(form.errors)

    else:
        form = ProjectRegistration()
    return render(request, 'submitProject.html', {'form': form, 'categories': categories, 'cities': cities})


def my_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.state != 0:
            if user.state == 1 or (user.isBen is False and user.isOrg is False):
                login(request, user)
                return HttpResponseRedirect('/')
            elif user.state is None:
                return render(request, 'userUnapproved.html')
        else:
            error = True
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')


@login_required
@benefactor_only
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


@login_required
@organization_only
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


@login_required
@admin_ben
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

        try:
            projects = projects.filter(budget__gte=int(request.POST.get('minimumbudget')))
        except ValueError:
            projects = projects.filter(budget__gte=0)

        try:
            projects = projects.filter(
                user__organizer__rate__totalRate__gte=int(request.POST.get('minimumtotalrating')))

        except ValueError:
            projects = projects.filter(user__organizer__rate__totalRate__gte=0)

        category = request.POST['field']
        if category != "blank":
            temp_projs = []
            for pr in projects:
                if len(CategoryProject.objects.filter(projectId=pr.id, categoryId=category)):
                    temp_projs.append(pr)

            projects = temp_projs

        return render(request, 'searchProject.html', {'projects': projects, 'categories': categories})
    else:
        projects = Project.objects.all()
        return render(request, 'searchProject.html', {'projects': projects, 'categories': categories})


@login_required
@admin_ben
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
            all_req = all_req.order_by('-NOPs')

        if sort_type == "participantsD":
            all_req = all_req.order_by('NOPs')

        try:
            all_req = all_req.filter(NOPs__gte=int(request.POST.get('minimumNOP')))
        except ValueError:
            all_req = all_req.filter(NOPs__gte=0)

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


@login_required
@admin_org
def list_abilities(request):
    name = request.POST.get('orgName', '')
    all_user_abilities = UserAbilities.objects.filter(username__benefactor__nickname__icontains=name)
    all_abilities = Ability.objects.all()
    user_abilities = []

    if request.method == 'POST':
        sort_type = request.POST['sortType']

        if sort_type == "rateD":
            all_user_abilities = all_user_abilities.order_by('-username__benefactor__rate__totalRate')

        if sort_type == "rateA":
            all_user_abilities = all_user_abilities.order_by('username__benefactor__rate__totalRate')

        if sort_type == "ageA":
            all_user_abilities = all_user_abilities.order_by('-username__benefactor__year')

        if sort_type == "ageD":
            all_user_abilities = all_user_abilities.order_by('username__benefactor__year')

        try:
            all_user_abilities = all_user_abilities.filter(
                username__benefactor__year__gte=int(request.POST.get('minimumAge', 0)))
        except ValueError:
            all_user_abilities = all_user_abilities.filter(username__benefactor__year__gte=0)

        try:
            all_user_abilities = all_user_abilities.filter(
                username__benefactor__rate__totalRate__gte=int(request.POST.get('minimumtotalrating', 0)))
        except ValueError:
            all_user_abilities = all_user_abilities.filter(username__benefactor__rate__totalRate__gte=0)

        ability = request.POST['field']
        if ability != "blank":
            temp_reqs = []
            for ua in all_user_abilities:
                if len(UserAbilities.objects.filter(username=ua.username, abilityId=ability)):
                    temp_reqs.append(ua)

            all_user_abilities = temp_reqs

    list = []

    for ua in all_user_abilities:
        if ua.username.username not in list:
            result = UserAbilities.objects.filter(username=ua.username.username)
            if len(result) != 0:
                user_abilities.append(result)
            list.append(ua.username.username)

    print(user_abilities)

    return render(request, 'searchAbilities.html', {'abilities': all_abilities, 'userAbilities': user_abilities})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username, state=True)
    if user.isBen:
        benefactor = Benefactor.objects.get(user=user)
        week = WeeklySchedule.objects.get(id=benefactor.wId.id)
        user_abilities = UserAbilities.objects.filter(username=user.username)
        orgs = Request.objects.filter(benefactorId=user, isAccepted=True)
        organizations = []
        for org in orgs:
            organizations.append(org.organizationId.organizer)

        if request.user.username == username:
            return render(request, 'personalProfileBenefactor.html',
                          {'user': user, 'benefactor': benefactor, 'week': week, 'user_abilities': user_abilities, 'organizations': organizations})
        else:
            return render(request, 'benefactorsProfileView.html',
                          {'user': user, 'benefactor': benefactor, 'week': week, 'user_abilities': user_abilities,
                           'rangee': range(28), 'organizations': organizations})
    elif user.isOrg:
        organization = Organizer.objects.get(user=user)
        projects = Project.objects.filter(user=user)
        requirements = Requirement.objects.filter(user=user)
        reqability = []
        bens = Request.objects.filter(organizationId=user, isAccepted=True)
        benefactors = []
        for ben in bens:
            benefactors.append(ben.benefactorId.benefactor)
        for req in requirements:
            reqability.append(RequirementAbilities.objects.filter(reqId=req))
        if request.user.username == username:
            return render(request, 'personalProfileOrganization.html',
                          {'user': user, 'org': organization, 'projects': projects, 'requirements': requirements,
                           'reqability': reqability, 'rangee': range(28), 'benefactors': benefactors})
        else:
            return render(request, 'organizationProfileView.html',
                          {'user': user, 'org': organization, 'projects': projects, 'requirements': requirements,
                           'reqability': reqability, 'rangee': range(28), 'benefactors': benefactors})


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


@login_required
def project(request, username, pId):
    user = get_object_or_404(CustomUser, username=username)
    organization = Organizer.objects.get(user=user)
    proj = get_object_or_404(Project, id=pId)
    return render(request, 'project.html', {'user': user, 'org': organization, 'project': proj})


@login_required
@organization_only
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

            return render(request, 'thanksSubmitRequirement.html')

        else:
            print(form.errors, week_form.errors)
    else:
        form = RequirementForm()
        week_form = WeekForm()

    return render(request, 'submitRequirement.html',
                  {'form': form, 'week_form': week_form, 'abilities': abilities, 'rangee': range(28), 'cities': cities})


@login_required
@admin_only
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


@login_required
@benefactor_only
def send_request_organization(request, username, reqId):
    if request.method == 'POST':
        user = CustomUser.objects.get(username=username)
        requirement = Requirement.objects.get(id=reqId)
        abilities = Ability.objects.all()
        desc = request.POST['description']
        if requirement.typeOfCooperation != 'atHome':
            weekForm = WeekForm(request.POST)
            week = weekForm.save()
            week.save()
            req = Request.objects.create(benefactorId=request.user, organizationId=user, wId=week,
                                         city=requirement.city,
                                         description=desc, reqId=requirement)
            Report.objects.create(benefactor=request.user, organization=user, type='2', description=desc, operator='1',
                                  date=datetime.datetime.today(), time=datetime.datetime.now(), wId=week, reqId=req)
        else:
            req = Request.objects.create(benefactorId=request.user, organizationId=user, isAtHome=True,
                                         city=requirement.city,
                                         description=desc, reqId=requirement)
            Report.objects.create(benefactor=request.user, organization=user, type='2', description=desc, operator='1',
                                  date=datetime.datetime.today(), time=datetime.datetime.now(), isAtHome=True,
                                  reqId=req)
        for a in abilities:
            name = a.name
            if request.POST.get(name) is not None:
                RequestAbilities.objects.create(reqId=req, abilityId=a)

        send_mail('پیشنهاد جدید', 'شما یک پیشنهاد جدید از طرف فلانی دارید', 'sender@mehraneh.com', [user.email])
        return render(request, 'thanks.html')


@login_required
@admin_only
def report_admin(request):
    reports = Report.objects.all()
    if request.method == 'POST':
        reports = Report.objects.all()
        try:
            reports = reports.filter(
                benefactor__benefactor__nickname__icontains=request.POST['beneName'])
        except ValueError:
            reports = reports

        try:
            reports = reports.filter(
                organization__organizer__name__icontains=request.POST['orgName'])
        except ValueError:
            reports = reports

        field = request.POST['field']
        if field != "blank":
            reports = reports.filter(type=field)
    return render(request, 'reportForAdmin.html', {'reports': reports})


@login_required
@organization_only
def send_request_benefactor(request, username):
    if request.method == 'POST':
        user = CustomUser.objects.get(username=username)
        abilities = Ability.objects.all()
        desc = request.POST['description']
        if user.benefactor.typeOfCooperation != 'atHome':
            weekForm = WeekForm(request.POST)
            week = weekForm.save()
            week.save()
            req = Request.objects.create(benefactorId=user, organizationId=request.user, wId=week, whoSubmit='2',
                                         city=user.benefactor.city, description=desc)
            Report.objects.create(benefactor=request.user, organization=user, type='2', description=desc, operator='2',
                                  date=datetime.datetime.today(), time=datetime.datetime.now(), wId=week, reqId=req)
        else:
            req = Request.objects.create(benefactorId=user, organizationId=request.user, isAtHome=True, whoSubmit='2',
                                         city=user.benefactor.city, description=desc)
            Report.objects.create(benefactor=request.user, organization=user, type='2', description=desc, operator='2',
                                  date=datetime.datetime.today(), time=datetime.datetime.now(), isAtHome=True,
                                  reqId=req)

        for a in abilities:
            name = a.name
            if request.POST.get(name) is not None:
                RequestAbilities.objects.create(reqId=req, abilityId=a)
        send_mail('پیشنهاد جدید', 'شما یک پیشنهاد جدید از طرف فلانی دارید', 'sender@mehraneh.com', [user.email])
        return render(request, 'thanks.html')


@login_required
def waiting_requests(request):
    requestsAbilities = []
    if request.user.isBen:
        requests = Request.objects.filter(benefactorId=request.user, whoSubmit='2', state=False)
    else:
        requests = Request.objects.filter(organizationId=request.user, whoSubmit='1', state=False)
    for req in requests:
        requestsAbilities.append(RequestAbilities.objects.filter(reqId=req))
    print(requestsAbilities)
    return render(request, 'waitingRequests.html', {'requestsAbilities': requestsAbilities})


@login_required
@organization_only
def report_cash(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'reportCash.html', {'projects': projects})


@login_required
@admin_only
def report_project(request, pId):
    project = get_object_or_404(Project, id=pId)
    reports = []
    if project.user == request.user:
        reports.append(Report.objects.filter(description=project.id, organization=project.user, type=3))
    return render(request, 'reportProject.html', {'project': project, 'reports': reports})


@login_required
@admin_only
def change_cities(request):
    cities = City.objects.all()
    if request.method == 'POST':
        if request.POST['type'] == "1":
            c = City.objects.create(name=request.POST['city'])
            c.save()
        else:
            c = City.objects.get(name=request.POST['city'])
            users = Benefactor.objects.filter(city=c.name)
            for user in users:
                user.city = "سایر"
                user.save()
            users = Organizer.objects.filter(city=c.name)
            for user in users:
                user.city = "سایر"
                user.save()
            users = Project.objects.filter(city=c.name)
            for user in users:
                user.city = "سایر"
                user.save()
            users = Requirement.objects.filter(city=c.name)
            for user in users:
                user.city = "سایر"
                user.save()
            c.delete()
        cities = City.objects.all()
        return render(request, 'changeCities.html', {'cities': cities})
    return render(request, 'changeCities.html', {'cities': cities})


@login_required
@admin_only
def change_categories(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        if request.POST['type'] == "1":
            c = Category.objects.create(name=request.POST['city'])
            c.save()
        else:
            c = Category.objects.get(name=request.POST['city'])
            c.delete()
        categories = Category.objects.all()
        return render(request, 'changeCategories.html', {'categories': categories})
    return render(request, 'changeCategories.html', {'categories': categories})


@login_required
@admin_only
def change_abilities(request):
    abilities = Ability.objects.all()
    if request.method == 'POST':
        if request.POST['type'] == "1":
            c = Ability.objects.create(name=request.POST['city'])
            c.save()
        else:
            c = Ability.objects.get(name=request.POST['city'])
            ua = UserAbilities.objects.filter(abilityId=c.id)
            for u in ua:
                u.delete()
            ra = RequirementAbilities.objects.filter(abilityId=c.id)
            for r in ra:
                r.delete()
            ra = RequestAbilities.objects.filter(abilityId=c.id)
            for r in ra:
                r.delete()
            c.delete()
        abilities = Ability.objects.all()
        return render(request, 'changeAbilities.html', {'abilities': abilities})
    return render(request, 'changeAbilities.html', {'abilities': abilities})


@login_required
def sent_requests(request):
    requestsAbilities = []
    if request.user.isBen:
        requests = Request.objects.filter(benefactorId=request.user, whoSubmit='1')
    else:
        requests = Request.objects.filter(organizationId=request.user, whoSubmit='2')
    for req in requests:
        requestsAbilities.append(RequestAbilities.objects.filter(reqId=req))
    print(requestsAbilities)
    return render(request, 'sentRequests.html', {'requestsAbilities': requestsAbilities})


@login_required
@admin_only
def remove_report(request, rId):
    report = Report.objects.get(id=rId)
    if report.type == '1':
        rate = report.rateId
        if report.operator == '1':
            totalRate = TotalRate.objects.get(id=report.benefactor.benefactor.rate.id)
            count = Rate.objects.filter(ratedUser=report.benefactor).count()
        elif report.operator == '2':
            totalRate = TotalRate.objects.get(id=report.organization.organizer.rate.id)
            count = Rate.objects.filter(ratedUser=report.organization).count()

        totalRate.f1 = ((totalRate.f1 * count) - ((rate.f1 - 1) / 4 * 100)) / (count - 1)
        totalRate.f2 = ((totalRate.f2 * count) - ((rate.f2 - 1) / 4 * 100)) / (count - 1)
        totalRate.f3 = ((totalRate.f3 * count) - ((rate.f3 - 1) / 4 * 100)) / (count - 1)
        totalRate.f4 = ((totalRate.f4 * count) - ((rate.f4 - 1) / 4 * 100)) / (count - 1)
        totalRate.f5 = ((totalRate.f5 * count) - ((rate.f5 - 1) / 4 * 100)) / (count - 1)
        totalRate.totalRate = round((totalRate.totalRate * count - (
            (rate.f1 - 1) / 4 + (rate.f2 - 1) / 4 + (rate.f3 - 1) / 4 + (rate.f4 - 1) / 4 + (
            rate.f5 - 1) / 4) / 5 * 100) / (count - 1), 1)
        totalRate.save()
        rate.delete()

    elif report.type == '2':
        req = report.reqId
        req.delete()

    report.delete()
    return HttpResponseRedirect('/reports')


@login_required
def accept_request(request):
    if request.method == 'POST':
        split = request.POST['req'].split('-')
        req = Request.objects.get(id=split[0])
        if split[1] == '1':
            req.isAccepted = True
            send_mail('تایید پیشنهاد', 'پیشنهاد شما تایید شده است!', 'sender@mehraneh.com', [request.user.email])
        else:
            req.isAccepted = False
        req.state = True
        req.save()
    return HttpResponseRedirect('/waiting_requests')


@login_required
def delete_user(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.POST['user'])
        if user.isBen:
            UserAbilities.objects.filter(username=user).delete()
            Request.objects.filter(benefactorId=user).delete()
            Report.objects.filter(benefactor=user).delete()
            Rate.objects.filter(ratedUser=user).delete()
            user.benefactor.delete()
        elif user.isOrg:
            Requirement.objects.filter(user=user).delete()
            Project.objects.filter(user=user).delete()
            Request.objects.filter(organizationId=user).delete()
            Report.objects.filter(organization=user).delete()
            Rate.objects.filter(ratedUser=user).delete()
            user.organizer.delete()
        user.state = False
        user.save()
        if request.user.isBen or request.user.isOrg:
            logout(request)
    return HttpResponseRedirect('/')