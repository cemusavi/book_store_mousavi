from django.urls import path, include

from . import views

app_name = 'address'

urlpatterns = [
    path('add/', views.AddAddress.as_view(), name='add_address'),
    path('api/', include('address.api.urls', namespace='address-api')),
]
