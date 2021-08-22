from django.contrib import admin
from . import models


class BookObjectInline(admin.TabularInline):
    model = models.BookObject


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    inlines = BookObjectInline,


@admin.register(models.BookObject)
class BookObjectAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = 'book', 'price', 'inventory', 'cash_discount', 'percent_discount'
    list_editable = 'price', 'inventory', 'percent_discount', 'cash_discount'
=======
    list_display = 'book', 'id', 'price', 'inventory', 'cash_discount', 'percent_discount'
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
