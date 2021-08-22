<<<<<<< HEAD
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.shortcuts import render
=======
from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.contrib.auth import views as auth_views
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4

from . import forms

User = get_user_model()


class RegisterUser(generic.CreateView):
    form_class = forms.RegisterForm
    queryset = User.objects.all()
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


<<<<<<< HEAD
=======
# class LoginUser(generic.View):
#
#     def _get_form(self):
#         self.form = forms.LoginForm(self.request.POST)
#         return self.form
#
#     def get(self, request):
#         form = self._get_form()
#         return render(request, 'login.html', {'form': form})
#
#     def post(self, request):
#         form = self._get_form()
#
#         if form.is_valid():
#             user = authenticate(**form.cleaned_data)
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#         return self.get(request)

>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
class PasswordReset(auth_views.PasswordResetView):
    template_name = 'password_reset.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'reset_mail_format.html'


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'password_reset_done.html'


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
<<<<<<< HEAD
    template_name = 'password_reset_complete.html'


class ProfileEdit(LoginRequiredMixin, generic.UpdateView):
    queryset = User.objects.all()
    form_class = forms.ProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


class ChangePassword(generic.View):

    def get_object(self):
        return self.request.user

    def get(self, request):
        form = forms.ChangePasswordForm()
        context = {
            'form': form
        }
        return render(request, 'change_password.html', context)
=======
    template_name = 'password_reset_complete.html'
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
