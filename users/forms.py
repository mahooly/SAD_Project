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
        fields = ('name', 'surname', 'nickname', 'gender', 'day', 'month', 'year', 'education', 'major', 'nationalId', 'city', 'address', 'phone', 'typeOfCooperation')


class OrganizationRegistration(forms.ModelForm):
    terms = forms.BooleanField(required=True)
    class Meta:
        model = Organization
        fields = ('name', 'address', 'phone', 'license', 'website', 'day', 'month', 'year', 'city')


class ProjectRegistration(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'budget', 'city', 'description', 'paymethod', 'cardno', 'accno')


class EditUser(forms.ModelForm):

    username = forms.CharField(max_length=30, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(widget=forms.PasswordInput, required=False)
    email = forms.EmailField(required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'password2', 'image')

    def clean(self):
        cleaned_data = super(EditUser, self).clean()
        confirm_password = cleaned_data.get('password2')
        password = cleaned_data.get('password')
        if not password == confirm_password and password != '':
            raise forms.ValidationError('Password does not match.')


class EditBenefactorProfile(forms.ModelForm):

    name = forms.CharField(max_length=20, required=False)
    surname = forms.CharField(max_length=30, required=False)
    nickname = forms.CharField(max_length=30, required=False)
    gender = forms.ChoiceField(choices=SEX_CHOICES, required=False)
    day = forms.CharField(max_length=2, required=False)
    month = forms.CharField(max_length=2, required=False)
    year = forms.CharField(max_length=4, required=False)
    education = forms.ChoiceField(choices=EDUCATION_CHOICES, required=False)
    major = forms.CharField(max_length=20, required=False)
    nationalId = forms.CharField(max_length=10, required=False)
    city = forms.CharField(max_length=10, required=False)
    address = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=12, required=False)
    typeOfCooperation = forms.ChoiceField(choices=COOP_CHOICES, required=False)

    class Meta:
        model = Benefactor
        fields = ('name', 'surname', 'nickname', 'gender', 'day', 'month', 'year', 'education', 'major', 'nationalId', 'city', 'address', 'phone', 'typeOfCooperation')


class EditOrganizationProfile(forms.ModelForm):

    name = forms.CharField(max_length=20, required=False)
    address = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=15, required=False)
    website = forms.URLField(required=False)
    license = forms.CharField(max_length=20, required=False)
    day = forms.CharField(max_length=2, required=False)
    month = forms.CharField(max_length=2, required=False)
    year = forms.CharField(max_length=4, required=False)
    city = forms.CharField(max_length=10, required=False)

    class Meta:
        model = Organization
        fields = ('name', 'address', 'phone', 'license', 'website', 'day', 'month', 'year', 'city')


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('f1', 'f2', 'f3', 'f3', 'f4', 'f5', 'description')


class WeekForm(forms.ModelForm):
    class Meta:
        model = WeeklySchedule
        exclude = ('id',)


class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        exclude = ('id', 'user', 'wId', 'NOPs',)


class AdminCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'password2', 'image', 'first_name', 'last_name')

    def clean(self):
        cleaned_data = super(AdminCreationForm, self).clean()
        confirm_password = cleaned_data.get('password2')
        password = cleaned_data.get('password')
        if not password == confirm_password:
            raise forms.ValidationError('Password does not match.')