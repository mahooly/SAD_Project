import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userTest.settings')

import django

django.setup()

import random
import re

from users.models import Benefactor
from users.models import CustomUser
from users.models import TotalRate
from users.models import Organization
from users.models import WeeklySchedule
from users.models import Project
from users.models import Requirement
from users.models import Ability
from users.models import UserAbilities
from users.models import RequirementAbilities
from users.models import Category
from users.models import CategoryProject
from users.models import Request
from faker import Faker


def make_users(valid_user, isben, n):
    fake_gen = Faker('fa_IR')

    for _ in range(n):
        fake_user = fake_gen.profile()
        username = fake_user['username'].replace('-', 'a')
        first_name = fake_user['name'].split()[0]
        last_name = fake_user['name'].split()[1]
        email = fake_user['mail']
        isorg = not isben
        state = valid_user

        CustomUser.objects.create(password='surftee', username=username,
                                  first_name=first_name, last_name=last_name,
                                  email=email, state=state,
                                  isBen=isben, isOrg=isorg)


def make_benefactor(n):
    make_users(None, True, n)
    fake_gen = Faker('fa_IR')
    counter = 0;
    for _ in range(n):
        fake_benefactor = fake_gen.profile()
        first_name = fake_benefactor['name'].split()[0]
        last_name = fake_benefactor['name'].split()[1]
        nick_name = fake_benefactor['name'].split()[-1]
        gender = random.choice(['male', 'female'])
        day = random.randint(1, 30)
        month = random.randint(1, 12)
        year = random.randint(40, 73)
        edu = random.choice(['diploma', 'master', 'bachelor', 'phd'])
        major = fake_benefactor['job']
        national_id = str(random.randint(120000, 999999))
        city = random.choice(['تهران', 'شیراز', 'مشهد', 'اصفهان'])
        address = fake_benefactor['address']
        phone = str(random.randint(1000000, 9999999))

        ben_users = CustomUser.objects.filter(isBen=True, isOrg=False)

        for u in ben_users:
            if counter < n and len(Benefactor.objects.filter(user=u)) == 0:
                try:
                    Benefactor.objects.create(user=u, name=first_name,
                                              surname=last_name, gender=gender,
                                              day=day, month=month,
                                              year=year, major=major,
                                              education=edu, nationalId=national_id,
                                              city=city, address=address,
                                              phone=phone, nickname=nick_name,
                                              wId_id=WeeklySchedule.objects.create(c2=random.choice(['on', 'off']),
                                                                                   c1=random.choice(['on', 'off']),
                                                                                   c3=random.choice(['on', 'off']),
                                                                                   c21=random.choice(['on', 'off']),
                                                                                   c12=random.choice(['on', 'off']),
                                                                                   c17=random.choice(['on', 'off'])).id,
                                              rate_id=TotalRate.objects.create(totalRate=random.randint(0, 100),
                                                                               f1=random.randint(0, 100),
                                                                               f2=random.randint(0, 100),
                                                                               f3=random.randint(0, 100),
                                                                               f4=random.randint(0, 100),
                                                                               f5=random.randint(0, 100)).id)
                    counter += 1
                    print('ben make done')
                    break

                except:
                    print('ben make error')
                    continue


def make_organization(n):
    make_users(None, False, n)
    fake_gen = Faker('fa_IR')
    counter = 0;
    for _ in range(n):
        fake_organization = fake_gen.profile()
        name = fake_organization['company']
        day = random.randint(1, 30)
        month = random.randint(1, 12)
        year = random.randint(30, 96)
        city = random.choice(['تهران', 'شیراز', 'مشهد', 'اصفهان'])
        address = fake_organization['address']
        phone = str(random.randint(1000000, 9999999))
        web = fake_organization['website'][0]
        license = str(random.randint(120000, 999999))

        org_users = CustomUser.objects.filter(isBen=False, isOrg=True)

        for u in org_users:
            if counter < n and len(Organization.objects.filter(user=u)) == 0:
                try:
                    Organization.objects.create(user=u, name=name,
                                                day=day, month=month,
                                                year=year, city=city,
                                                address=address, phone=phone,
                                                website=web, license=license,
                                                rate_id=TotalRate.objects.create(totalRate=random.randint(0, 100),
                                                                                 f1=random.randint(0, 100),
                                                                                 f2=random.randint(0, 100),
                                                                                 f3=random.randint(0, 100),
                                                                                 f4=random.randint(0, 100),
                                                                                 f5=random.randint(0, 100)).id)
                    counter += 1
                    print('org make done')
                    break

                except:
                    print('org make error')
                    continue


def make_project(n):
    fake_gen = Faker('fa_IR')
    for _ in range(n):
        fake_project = fake_gen.profile()
        name = "پروژه خیرانه " + fake_project['job'] + " " + (fake_project['company'].split()[0]) + " "
        budget = random.randint(5000, 100000)
        city = random.choice(['تهران', 'شیراز', 'مشهد', 'اصفهان'])
        desciption = "پروژه‌ای خیرانه برای کمک"
        paymethod = random.choice(['1', '2'])
        cardn = str(random.randint(12312312, 797899679))
        accn = str(random.randint(12312312, 797899679))
        alrdpaid = budget - random.randint(0, budget)

        orgs = CustomUser.objects.filter(isOrg=True)

        rnd = random.randint(0, len(orgs))
        user = orgs[rnd]

        Project.objects.create(user=user, name=name, budget=budget, city=city,
                               description=desciption, paymethod=paymethod,
                               cardno=cardn, accno=accn, alreadyPaid=alrdpaid)

        print('proj make done')


def make_requirement(n):
    fake_gen = Faker('fa_IR')
    for _ in range(n):
        fake_requirement = fake_gen.profile()
        name = "نیازمندی " + fake_requirement['job'] + " " + (fake_requirement['company'].split()[0]) + " "
        city = random.choice(['تهران', 'شیراز', 'مشهد', 'اصفهان'])
        desciption = "نیازمند افرادی برای یاری"
        nop = random.randint(2, 25)

        orgs = CustomUser.objects.filter(isOrg=True)

        rnd = random.randint(0, len(orgs))
        user = orgs[rnd]

        Requirement.objects.create(user=user, name=name, city=city,
                                   description=desciption,
                                   wId_id=WeeklySchedule.objects.create(c2=random.choice(['on', 'off']),
                                                                        c1=random.choice(['on', 'off']),
                                                                        c3=random.choice(['on', 'off']),
                                                                        c21=random.choice(['on', 'off']),
                                                                        c12=random.choice(['on', 'off']),
                                                                        c17=random.choice(['on', 'off'])).id,

                                   NOPs=nop)

        print('req make done')


def make_ability(n):
    for _ in range(n):
        name = random.choice(
            ['خیاطی', 'کارگری', 'جوشکاری', 'کفاشی', 'منابع انسانی', 'مدریت راهبردی', 'معلم', 'مکانیک', 'پزشکی',
             'آتش نشان', 'نگهبان', 'برق کار'])
        Ability.objects.get_or_create(name=name)
        print('ab make done')


def make_user_ability(n):
    users = CustomUser.objects.filter(isBen=True)
    abils = Ability.objects.all()
    counter = 0;
    for _ in range(n ** 2):
        rnd_abils = random.randint(0, len(abils))
        rnd_users = random.randint(0, len(users))
        if counter < n:
            try:
                UserAbilities.objects.create(abilityId=abils[rnd_abils], username=users[rnd_users])
                print("us_ab make done")
                counter += 1
            except:
                print("us_ab make error")


def make_requirement_ability(n):
    reqs = Requirement.objects.all()
    abils = Ability.objects.all()
    counter = 0;
    for _ in range(n ** 2):
        rnd_abils = random.randint(0, len(abils))
        rnd_reqs = random.randint(0, len(reqs))
        if counter < n:
            try:
                RequirementAbilities.objects.create(abilityId=abils[rnd_abils], reqId=reqs[rnd_reqs])
                print("rq_ab make done")
                counter += 1
            except:
                print("rq_ab make error")


def make_category(n):
    for _ in range(n):
        name = random.choice(
            ['صنعتی', 'بشردوستانه', 'درازمدت', 'محیط زیست', 'تحقیقاتی', 'زیرساختی', 'منابع'])
        Category.objects.get_or_create(name=name)
        print('cat make done')


def make_category_project(n):
    projs = Project.objects.all()
    cats = Category.objects.all()
    for _ in range(n):
        rnd_proj = random.randint(0, len(projs))
        rnd_cats = random.randint(0, len(cats))
        try:
            CategoryProject.objects.create(categoryId=cats[rnd_cats], projectId=projs[rnd_proj])
            print("cat_proj make done")

        except:
            print("cat_proj make error")


def make_request(n):
    orgs = CustomUser.objects.filter(isOrg=True)
    bens = CustomUser.objects.filter(isBen=True)
    reqs = Requirement.objects.all()

    counter = 0
    for o in orgs:
        reqs = Requirement.objects.all()
        rnd_bens = random.randint(0, len(bens))
        city = random.choice(['تهران', 'شیراز', 'مشهد', 'اصفهان'])
        desc = 'اگر دوست دارید همکاری کنیم. باتشکر'

        reqs = reqs.filter(user=o)
        if len(reqs) != 0:
            rnd_reqs = random.randint(0, len(reqs))
            print("ioi")
            if counter < n:
                Request.objects.get_or_create(benefactorId=bens[rnd_bens-1], reqId=reqs[rnd_reqs-1], organizationId=o,
                                              city=city, description=desc,
                                              wId_id=WeeklySchedule.objects.create(c2=random.choice(['on', 'off']),
                                                                                   c1=random.choice(['on', 'off']),
                                                                                   c3=random.choice(['on', 'off']),
                                                                                    c21=random.choice(['on', 'off']),
                                                                                   c12=random.choice(['on', 'off']),
                                                                                   c17=random.choice(['on', 'off'])).id)
                print('request make done')
                counter+=1

make_request(30)
