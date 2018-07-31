from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import *

admin_required = user_passes_test(lambda u: (not u.isBen and not u.isOrg), login_url='404')

admin_or_benefactor_required = user_passes_test(lambda u: (u.isBen or (not u.isBen and not u.isOrg)), login_url='404')

admin_or_organization_required = user_passes_test(lambda u: (u.isOrg or (not u.isBen and not u.isOrg)), login_url='404')


def admin_only(view_func):
    decorated_view_func = login_required(admin_required(view_func))
    return decorated_view_func


def admin_org_only(view_func):
    decorated_view_func = login_required(admin_or_organization_required(view_func))
    return decorated_view_func


def admin_ben_only(view_func):
    decorated_view_func = login_required(admin_or_benefactor_required(view_func))
    return decorated_view_func


def handler404(request):
    return render(request, 'main/404.html', status=404)


def handler500(request):
    return render(request, 'main/500.html', status=500)


def index(request):
    orgs = Organization.objects.all().order_by('-rate__totalRate')[:4]
    bens = Benefactor.objects.all().order_by('-rate__totalRate')[:4]
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
    return render(request, 'main/index.html',
                  {'bens': bens, 'orgs': orgs, 'orgProjects': orgProjects, 'benAbilities': benAbilities,
                   'ratingOrg': ratingOrg, 'ratingBens': ratingBens, 'orgRequirements': orgRequirements})


def terms(request):
    return render(request, 'main/terms.html')


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
            if request.user.username != '' and request.user.is_authorized and not request.user.isBen and not request.user.isOrg:
                user.state = True
            user.save()
            rate = TotalRate.objects.create()
            benefactor = form.save(commit=False)
            benefactor.user = user
            week = week_form.save()
            week.save()
            benefactor.wId = week
            benefactor.rate = rate
            benefactor.save()

            for a in abilities:
                name = a.name
                if request.POST.get(name) is not None:
                    UserAbilities.objects.create(abilityId=a, username=user)

            return render(request, 'registration/thanks.html')

        else:
            print(user_form.errors, form.errors)

    else:
        user_form = UserForm()
        form = BenefactorRegistraton()
        week_form = WeekForm()
    cities = City.objects.all()
    return render(request, 'registration/registerBenefactor.html',
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
            if request.user.username != '' and request.user.is_authorized and not request.user.isBen and not request.user.isOrg:
                user.state = True
            user.save()
            organizer = form.save(commit=False)
            organizer.user = user
            organizer.rate = TotalRate.objects.create()
            organizer.save()

            return render(request, 'registration/thanks.html')

        else:
            print(user_form.errors, form.errors)

    else:
        user_form = UserForm()
        form = BenefactorRegistraton()

    return render(request, 'registration/registerOrganization.html',
                  {'user_form': user_form, 'form': form, 'cities': cities})


@admin_org_only
def project_creation(request):
    categories = Category.objects.all()
    cities = City.objects.all()
    if request.method == 'POST':
        form = ProjectRegistration(request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.save()

            for c in categories:
                name = c.name
                if request.POST.get(name) is not None:
                    CategoryProject.objects.create(categoryId=c, projectId=new_project)

            return render(request, 'registration/thanksSubmitProject.html')

        else:
            print(form.errors)

    else:
        form = ProjectRegistration()
    return render(request, 'registration/submitProject.html',
                  {'form': form, 'categories': categories, 'cities': cities})


def my_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.state != 0:
            if user.state == 1 or (user.isBen is False and user.isOrg is False):
                login(request, user)
                return HttpResponseRedirect('/')
            elif user.state is None:
                return render(request, 'registration/userUnapproved.html')
        else:
            error = True
            return render(request, 'registration/login.html', {'error': error})
    else:
        return render(request, 'registration/login.html')


@admin_ben_only
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

    return render(request, 'profile/editProfileBenefactor.html',
                  {'user_form': user_form, 'form': form, 'week_form': week_form, 'abilities': abilities, 'user': user,
                   'person': benefactor, 'week': week, 'user_abilities': user_abilities, 'rangee': range(28),
                   'cities': cities})


@admin_org_only
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
            organization = Organization.objects.get(user=user)
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

    return render(request, 'profile/editProfileOrganization.html',
                  {'user_form': user_form, 'form': form, 'user': user, 'org': organization, 'cities': cities})


@admin_ben_only
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

        tmp = []
        minrate = request.POST.get('minimumtotalrating')
        if minrate is not None:
            for p in projects:
                count = Rate.objects.filter(ratedUser=p.user).count()
                if count == 0 or p.user.organizer.rate.totalRate >= float(minrate) * 25:
                    tmp.append(p)
        projects = tmp

        category = request.POST['field']
        if category != "blank":
            temp_projs = []
            for pr in projects:
                if len(CategoryProject.objects.filter(projectId=pr.id, categoryId=category)):
                    temp_projs.append(pr)

            projects = temp_projs
    else:
        projects = Project.objects.all()
    return render(request, 'main/searchProject.html', {'projects': projects, 'categories': categories})


@admin_ben_only
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
            tmp = []
            minrate = request.POST.get('minimumtotalrating')
            if minrate is not None:
                for req in all_req:
                    count = Rate.objects.filter(ratedUser=req.user).count()
                    if count == 0 or req.user.organizer.rate.totalRate >= (float(minrate) - 1) * 25:
                        tmp.append(req)
            all_req = tmp
        except ValueError:
            pass

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

    return render(request, 'main/searchRequirement.html', {'abilities': all_ab, 'reqAbilities': req_ab})


@admin_org_only
def list_abilities(request):
    name = request.POST.get('orgName', '')
    all_user_abilities = UserAbilities.objects.filter(username__benefactor__nickname__icontains=name,
                                                      username__state=True)
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
            tmp = []
            minrate = request.POST.get('minimumtotalrating')
            if minrate is not None:
                for ua in all_user_abilities:
                    count = Rate.objects.filter(ratedUser=ua.username).count()
                    if count == 0 or ua.username.benefactor.rate.totalRate >= (float(minrate) - 1) * 25:
                        tmp.append(ua)
            all_user_abilities = tmp
        except ValueError:
            pass

        ability = request.POST['field']
        if ability != "blank":
            temp_reqs = []
            for ua in all_user_abilities:
                if len(UserAbilities.objects.filter(username=ua.username, abilityId=ability)):
                    temp_reqs.append(ua)

            all_user_abilities = temp_reqs

    temp_list = []

    for ua in all_user_abilities:
        if ua.username.username not in temp_list:
            result = UserAbilities.objects.filter(username=ua.username.username)
            if len(result) != 0:
                user_abilities.append(result)
            temp_list.append(ua.username.username)

    return render(request, 'main/searchAbilities.html', {'abilities': all_abilities, 'userAbilities': user_abilities})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username, state=True)
    count = Rate.objects.filter(ratedUser=user).count()
    if user.isBen:
        benefactor = Benefactor.objects.get(user=user)
        week = WeeklySchedule.objects.get(id=benefactor.wId.id)
        user_abilities = UserAbilities.objects.filter(username=user.username)
        orgs = Request.objects.filter(benefactorId=user, isAccepted=True)
        comments = Report.objects.filter(benefactor=user, type=1, operator=2)
        organizations = []
        for org in orgs:
            organizations.append(org.organizationId.organizer)

        if request.user.username == username:
            return render(request, 'profile/personalProfileBenefactor.html',
                          {'user': user, 'benefactor': benefactor, 'week': week, 'user_abilities': user_abilities,
                           'organizations': organizations, 'count': count, 'comments': comments})
        else:
            return render(request, 'profile/benefactorsProfileView.html',
                          {'user': user, 'benefactor': benefactor, 'week': week, 'user_abilities': user_abilities,
                           'rangee': range(28), 'organizations': organizations, 'count': count, 'comments': comments})
    elif user.isOrg:
        organization = Organization.objects.get(user=user)
        projects = Project.objects.filter(user=user)
        requirements = Requirement.objects.filter(user=user)
        comments = Report.objects.filter(organization=user, type=1, operator=1)
        reqability = []
        bens = Request.objects.filter(organizationId=user, isAccepted=True)
        benefactors = []
        for ben in bens:
            benefactors.append(ben.benefactorId.benefactor)
        for req in requirements:
            reqability.append(RequirementAbilities.objects.filter(reqId=req))
        if request.user.username == username:
            return render(request, 'profile/personalProfileOrganization.html',
                          {'user': user, 'org': organization, 'projects': projects, 'requirements': requirements,
                           'reqability': reqability, 'rangee': range(28), 'benefactors': benefactors, 'count': count,
                           'comments': comments})
        else:
            return render(request, 'profile/organizationProfileView.html',
                          {'user': user, 'org': organization, 'projects': projects, 'requirements': requirements,
                           'reqability': reqability, 'rangee': range(28), 'benefactors': benefactors, 'count': count,
                           'comments': comments})


@login_required
def rate_user(request, username):
    user = get_object_or_404(CustomUser, username=username, state=True)
    if request.method == 'POST':
        form = RateForm(request.POST)
        rate = form.save(commit=False)
        rate.user = request.user
        rate.ratedUser = user
        rate.save()
        description = request.POST['description']
        if user.isBen:
            totalRate = TotalRate.objects.get(id=user.benefactor.rate.id)
            Report.objects.create(benefactor=user, organization=request.user, type='1', operator='2', rateId=rate,
                                  date=datetime.datetime.today(), time=datetime.datetime.now(), payment=0,
                                  description=description)
        else:
            totalRate = TotalRate.objects.get(id=user.organizer.rate.id)
            Report.objects.create(benefactor=request.user, organization=user, type='1', operator='1', rateId=rate,
                                  date=datetime.datetime.today(), time=datetime.datetime.now(), payment=0,
                                  description=description)

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
        return render(request, 'profile/thanksSubmitComment.html', {'user': user})

    else:
        form = RateForm()
        if user.isBen:
            benefactor = Benefactor.objects.get(user=user)
            return render(request, 'profile/comment.html', {'user': user, 'benefactor': benefactor, 'form': form})
        else:
            organization = Organization.objects.get(user=user)
            return render(request, 'profile/comment.html', {'user': user, 'organization': organization, 'form': form})


@login_required
def project(request, username, p_id):
    user = get_object_or_404(CustomUser, username=username, state=True)
    organization = Organization.objects.get(user=user)
    proj = get_object_or_404(Project, id=p_id)
    return render(request, 'project.html', {'user': user, 'org': organization, 'project': proj})


@admin_org_only
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

            return render(request, 'registration/thanksSubmitRequirement.html')

        else:
            print(form.errors, week_form.errors)
    else:
        form = RequirementForm()
        week_form = WeekForm()

    return render(request, 'registration/submitRequirement.html',
                  {'form': form, 'week_form': week_form, 'abilities': abilities, 'rangee': range(28), 'cities': cities})


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
    return render(request, 'admin/waitingRegisters.html', {'users': users})


@admin_ben_only
def send_request_organization(request, username, req_id):
    if request.method == 'POST':
        user = CustomUser.objects.get(username=username)
        requirement = Requirement.objects.get(id=req_id)
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
        return render(request, 'profile/thanksSubmitRequest.html')


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
    return render(request, 'admin/reportForAdmin.html', {'reports': reports})


@admin_org_only
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
        return render(request, 'profile/thanksSubmitRequest.html')


@login_required
def waiting_requests(request):
    requestsAbilities = []
    if request.user.isBen:
        requests = Request.objects.filter(benefactorId=request.user, whoSubmit='2', state=False)
    else:
        requests = Request.objects.filter(organizationId=request.user, whoSubmit='1', state=False)
    for req in requests:
        requestsAbilities.append(RequestAbilities.objects.filter(reqId=req))
    return render(request, 'profile/waitingRequests.html', {'requestsAbilities': requestsAbilities})


@admin_org_only
def report_cash(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'main/reportCash.html', {'projects': projects})


def report_project(request, p_id):
    get_project = get_object_or_404(Project, id=p_id)
    reports = []
    if get_project.user == request.user:
        reports = Report.objects.filter(description=get_project.id, organization=get_project.user, type=3)
    return render(request, 'admin/reportProject.html', {'project': get_project, 'reports': reports})


@admin_only
def change_cities(request):
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
            users = Organization.objects.filter(city=c.name)
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
    return render(request, 'admin/changeCities.html', {'cities': cities})


@admin_only
def change_categories(request):
    if request.method == 'POST':
        if request.POST['type'] == "1":
            c = Category.objects.create(name=request.POST['city'])
            c.save()
        else:
            c = Category.objects.get(name=request.POST['city'])
            c.delete()
    categories = Category.objects.all()
    return render(request, 'admin/changeCategories.html', {'categories': categories})


@admin_only
def change_abilities(request):
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
    return render(request, 'admin/changeAbilities.html', {'abilities': abilities})


@login_required
def sent_requests(request):
    requestsAbilities = []
    if request.user.isBen:
        requests = Request.objects.filter(benefactorId=request.user, whoSubmit='1')
    else:
        requests = Request.objects.filter(organizationId=request.user, whoSubmit='2')
    for req in requests:
        r = RequestAbilities.objects.filter(reqId=req)
        if len(r) > 0:
            requestsAbilities.append(r)
    return render(request, 'profile/sentRequests.html', {'requestAbilities': requestsAbilities})


@admin_only
def remove_report(request, r_id):
    report = Report.objects.get(id=r_id)
    if report.type == '1':
        rate = report.rateId
        if report.operator == '1':
            totalRate = TotalRate.objects.get(id=report.organization.organizer.rate.id)
            count = Rate.objects.filter(ratedUser=report.organization).count()
        elif report.operator == '2':
            totalRate = TotalRate.objects.get(id=report.benefactor.benefactor.rate.id)
            count = Rate.objects.filter(ratedUser=report.benefactor).count()

        totalRate.f1 = ((totalRate.f1 * count) - ((rate.f1 - 1) / 4 * 100)) / (count - 1)
        totalRate.f2 = ((totalRate.f2 * count) - ((rate.f2 - 1) / 4 * 100)) / (count - 1)
        totalRate.f3 = ((totalRate.f3 * count) - ((rate.f3 - 1) / 4 * 100)) / (count - 1)
        totalRate.f4 = ((totalRate.f4 * count) - ((rate.f4 - 1) / 4 * 100)) / (count - 1)
        totalRate.f5 = ((totalRate.f5 * count) - ((rate.f5 - 1) / 4 * 100)) / (count - 1)
        totalRate.totalRate = round((totalRate.f1 + totalRate.f2 + totalRate.f3 + totalRate.f4 + totalRate.f5) / 5, 1)
        totalRate.save()
        rate.delete()

    elif report.type == '2':
        req = report.reqId
        req.delete()

    report.delete()
    return HttpResponseRedirect('/admin/reports')


@login_required
def accept_request(request):
    if request.method == 'POST':
        split = request.POST['req'].split('-')
        req = Request.objects.get(id=split[0])
        if split[1] == '1':
            req.isAccepted = True
            if req.whoSubmit == '1':
                req.reqId.NOPs += 1
                req.reqId.save()
            send_mail('تایید پیشنهاد', 'پیشنهاد شما تایید شده است!', 'sender@mehraneh.com', [request.user.email])
        else:
            req.isAccepted = False
        req.state = True
        req.save()
    return HttpResponseRedirect('/requests/pending')


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


@admin_only
def delete_requirement(request):
    if request.method == 'POST':
        req = Requirement.objects.get(id=request.POST['deletedReq'])
        RequirementAbilities.objects.filter(reqId=req.id).delete()
        Request.objects.filter(reqId=req.id).delete()
        req.delete()
    return render(request, 'admin/thanksDeleteReq.html')


@admin_only
def delete_project(request):
    if request.method == 'POST':
        project_delete = Project.objects.get(id=request.POST['deletedProj'])
        CategoryProject.objects.filter(projectId=project_delete.id).delete()
        project_delete.delete()
    return render(request, 'admin/thanksDeleteProj.html')


@admin_org_only
def delete_request(request, req_id):
    if request.method == 'POST':
        req = Request.objects.get(id=req_id)
        req.delete()
    return HttpResponseRedirect('/requests/sent')


@login_required
def donate(request):
    if request.method == 'POST':
        p_id = request.POST['projectId']
        value = request.POST['value']
        project_donate = Project.objects.get(id=p_id)
        if project_donate is None:
            return render(request, 'main/404.html', status=404)
        else:
            project_donate.alreadyPaid += int(value)
            project_donate.save()
            r = Report.objects.create(benefactor=request.user, organization=project_donate.user, type=3,
                                      description=project_donate.id,
                                      operator=1,
                                      date=datetime.datetime.today(), time=datetime.datetime.now(), payment=value)
            r.save()
        return render(request, 'registration/thanksDonateProject.html', {'org': project_donate.user.organizer})


@admin_org_only
def change_project(request, p_id):
    if request.method == 'POST':
        project_change = Project.objects.get(id=p_id)
        project_change.budget = request.POST['budget']
        project_change.description = request.POST['description']
        project_change.save()
    return render(request, 'registration/thanksSubmitProject.html')


@admin_org_only
def change_requirement(request, req_id):
    if request.method == 'POST':
        week_form = WeekForm(request.POST)
        if week_form.is_valid():
            week = week_form.save()
            week.save()
            requirement = Requirement.objects.get(id=req_id)
            requirement.address = request.POST['address']
            requirement.description = request.POST['description']
            requirement.wId = week
            requirement.save()
    return render(request, 'registration/thanksSubmitRequirement.html')


def admin_registration(request):
    if request.method == 'POST':
        form = AdminCreationForm(request.POST, request.FILES)
        if form.is_valid():
            admin = form.save()
            admin.set_password(admin.password)
            admin.is_staff = True
            admin.state = True
            admin.save()
        else:
            print(form.errors)

    else:
        form = AdminCreationForm()

    return render(request, 'registration/createAdmin.html', {'form': form})
