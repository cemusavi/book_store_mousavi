from django.urls import path, include

app_name = 'discount'

urlpatterns = [
    path('api/', include('discount.api.urls', namespace='discount-api'))
]
