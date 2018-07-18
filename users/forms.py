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
    terms = forms.BooleanField(required=True)
    class Meta:
        model = Benefactor
        fields = ('name', 'surname', 'nickname', 'gender', 'day', 'month', 'year', 'education', 'major', 'nationalId', 'city', 'address', 'phone')


class OrganizationRegistration(forms.ModelForm):
    terms = forms.BooleanField(required=True)
    class Meta:
        model = Organizer
        fields = ('name', 'address', 'phone', 'license', 'website', 'day', 'month', 'year', 'city')


class ProjectRegistration(forms.ModelForm):
    terms = forms.BooleanField(required=True)
    class Meta:
        model = Project
        fields = ('name', 'budget', 'city', 'description', 'paymethod', 'cardno', 'accno')


class EditUser(forms.ModelForm):

    username = forms.CharField(max_length=30, required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=False)
    image = forms.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'password2', 'image')


class EditBenefactorProfile(forms.ModelForm):

    name = forms.CharField(max_length=20, required=False)
    surname = forms.CharField(max_length=30, required=False)
    nickname = forms.CharField(max_length=30, required=False)
    gender = forms.ChoiceField(choices=SEX_CHOICES, required=False)
    class Meta:
        model = Benefactor
        fields = ('name', 'surname', 'nickname', 'gender')


class EditOrganizationProfile(forms.ModelForm):

    name = forms.CharField(max_length=20, required=False)
    address = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=15, required=False)
    website = forms.URLField(required=False)
    license = forms.CharField(max_length=20, required=False)
    class Meta:
        model = Organizer
        fields = ('name', 'address', 'phone', 'license', 'website')


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('f1', 'f2', 'f3', 'f3', 'f4', 'f5', 'description')


class WeekForm(forms.ModelForm):
    class Meta:
        model = WeeklySchedule
        exclude = ('id',)

