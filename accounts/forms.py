<<<<<<< HEAD
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
=======
<<<<<<< HEAD
from django import forms
from django.contrib.auth import get_user_model
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4

from address import models

User = get_user_model()


class RegisterForm(forms.ModelForm):
    repeat_password = forms.CharField(widget=forms.PasswordInput())
    city = forms.CharField()
    exact_address = forms.CharField()

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'repeat_password',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'avatar',
            'city',
            'exact_address',
        )

    def clean(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['repeat_password']
        if not password == re_password:
            raise forms.ValidationError('Passwords must match')
        data = self.cleaned_data
        data.pop('repeat_password')
        return data

    def clean_username(self):
        username = self.cleaned_data['username']
        que = User.objects.filter(username=username)
        if que:
            raise forms.ValidationError('Username is Already taken!')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        que = User.objects.filter(email=email)
        if que:
            raise forms.ValidationError('email is Already taken!')
        return email

    def save(self, commit=True):
        data = self.cleaned_data
        city = data.pop('city')
        exact_address = data.pop('exact_address')
        instance = User.objects.create_user(**data)
        models.Address.objects.create(
            user=instance,
            city=city,
            exact_address=exact_address
        )
        return instance


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
<<<<<<< HEAD


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'avatar',
        )


class ChangePasswordForm(forms.Form):
    previous_password = forms.CharField()
    new_password = forms.CharField(widget=forms.PasswordInput())
    repeat_new_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        data = self.cleaned_data
        password = data.get('new_password')
        re_pass = data.get('repeat_new_password')
        if password != re_pass:
            raise forms.ValidationError(_('Passwords dont match!'))
        return data

=======
=======
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
>>>>>>> d48277e8718ded697aae5e131e4f35d5c59606b4
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
