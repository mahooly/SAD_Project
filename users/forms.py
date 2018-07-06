from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'isBen', 'isOrg', 'image')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'password2', 'image')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        confirm_password = cleaned_data.get('password2')
        password = cleaned_data.get('password')
        if not password == confirm_password:
            raise forms.ValidationError('Password does not match.')


class BenefactorRegistraton(forms.ModelForm):
    class Meta:
        model = Benefactor
        fields = ('name', 'surname', 'nickname', 'gender')


class OrganizationRegistration(forms.ModelForm):
    terms = forms.BooleanField(required=True)
    class Meta:
        model = Organizer
        fields = ('name', 'address', 'phone', 'license', 'website')


class ProjectRegistration(forms.ModelForm):
    terms = forms.BooleanField(required=True)
    class Meta:
        model = Project
        fields = ('name', 'budget', 'city', 'description', 'paymethod', 'cardno', 'accno')