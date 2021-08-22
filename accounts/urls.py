<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
<<<<<<< HEAD
    path('api/', include('accounts.api.urls', namespace='accounts-api')),
=======
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
<<<<<<< HEAD
    path('edit_profile/', views.ProfileEdit.as_view(), name='edit_profile'),
    path('change_password/', views.ChangePassword.as_view(), name='change_password'),
=======
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
]
