from django.urls import path
from . import views

app_name = 'discount-api'

urlpatterns = [
    path('', views.ApplyDiscount.as_view(), name='apply-discount'),
]
