from django.urls import path
from . import views

app_name = 'order-api'

urlpatterns = [
    path('create/', views.AddOrderDetail.as_view(), name='order-create'),
    path('update/', views.UpdateOrderDetail.as_view(), name='update-order-detail'),
]
