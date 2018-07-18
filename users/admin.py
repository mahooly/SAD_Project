from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'isBen', 'isOrg', 'image']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Benefactor)
admin.site.register(Organizer)
admin.site.register(Project)
admin.site.register(Ability)
admin.site.register(UserAbilities)

