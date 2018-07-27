from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'isBen', 'isOrg', 'image', 'state']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Benefactor)
admin.site.register(Organizer)
admin.site.register(Project)
admin.site.register(Ability)
admin.site.register(UserAbilities)
admin.site.register(WeeklySchedule)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(CategoryProject)
admin.site.register(Requirement)
admin.site.register(RequirementAbilities)
admin.site.register(Report)
admin.site.register(Rate)
admin.site.register(TotalRate)
admin.site.register(Request)


