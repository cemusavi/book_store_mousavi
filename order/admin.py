<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
from django.contrib import admin
from . import models


class OrderDetailInline(admin.TabularInline):
    model = models.OrderDetail


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = OrderDetailInline,
<<<<<<< HEAD
    list_display = 'user', 'is_paid', 'payment_date', 'address', 'cash_discount', 'percent_discount'
=======
    list_display = 'user', 'is_paid', 'payment_date', 'address'
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4


@admin.register(models.OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = 'order', 'book', 'quantity'
<<<<<<< HEAD
=======
=======
from django.contrib import admin
import order.models
admin.site.register(order.models.Address)
admin.site.register(order.models.Order)
admin.site.register(order.models.OrderItem)
admin.site.register(order.models.Product)
admin.site.register(order.models.Category)
admin.site.register(order.models.CashDiscount)
admin.site.register(order.models.PrecentedDiscount)
>>>>>>> d48277e8718ded697aae5e131e4f35d5c59606b4
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4
