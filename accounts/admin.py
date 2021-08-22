<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
import re

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.utils.datetime_safe import datetime

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = 'username', 'email', 'first_name', 'last_name', 'phone_number'
    fieldsets = (
        ('Personal', {
            'fields': ('first_name', 'last_name', 'phone_number', 'avatar')
        }),
        ('Account', {
            'fields': ('username', 'password', 'email',)
        }),
        ('Security', {
<<<<<<< HEAD
            'fields': ('is_staff', 'is_superuser','groups'),
=======
            'fields': ('is_staff', 'is_superuser'),
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
        }),
    )

    @staticmethod
    def _check_pass(password):
        patt = r'^pbkdf2_sha256'
        if re.match(patt, password):
            return True
        return False

    def save_model(self, request, obj, form, change):
        password = form.cleaned_data['password']
        if not self._check_pass(password):
            obj.password = make_password(password)
        obj.save()
<<<<<<< HEAD
=======
=======
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]


admin.site.register(CustomUser, CustomUserAdmin)
>>>>>>> d48277e8718ded697aae5e131e4f35d5c59606b4
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
