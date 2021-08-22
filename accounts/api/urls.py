from django.urls import path
from accounts.api import views

app_name = 'accounts-api'

urlpatterns = [
    path('change/', views.ChangePassword.as_view(), name='change_password'),
]
