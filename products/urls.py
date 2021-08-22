from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductList.as_view(), name='products'),
    path('search/', views.ProductSearchList.as_view(), name='search'),
    path('<slug:slug>/', views.ProductDetail.as_view(), name='products-detail'),
]
