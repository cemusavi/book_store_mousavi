from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = 'order'

urlpatterns = [
    path('', views.OrderCreate.as_view(), name='order-create'),
    path('api/', include('order.api.urls', namespace='order-api')),
    path('control/', views.ControlOrder.as_view(), name='control-order'),
    path('confirm_order/<int:pk>', views.ConfirmOrder.as_view(), name='confirm-order'),
    path('congratulations/', TemplateView.as_view(template_name='congratulations.html'), name='congratulations'),
    path('order-history/',views.OrderHistory.as_view(),name='order-history'),
]
