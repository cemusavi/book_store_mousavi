from django.urls import path
from address.api import views

app_name = 'address-api'

urlpatterns = [
    path('add/', views.AddAddress.as_view(), name='add_address'),
]
