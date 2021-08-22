from django.contrib import admin

from . import models


@admin.register(models.Percent)
class PercentAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = 'percent','expiration_date',
    list_display_links = 'percent',
    list_editable = 'expiration_date',
=======
    pass
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4


@admin.register(models.PercentCode)
class PercentCodeAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = 'percent', 'expiration_date','code'
    list_display_links = 'percent',
    list_editable = 'expiration_date','code'
=======
    pass
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4


@admin.register(models.SpecificPercent)
class SpecificPercentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Cash)
class CashAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = 'cash', 'expiration_date',
    list_display_links = 'cash',
    list_editable = 'expiration_date',
=======
    pass
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4


@admin.register(models.CashCode)
class CashCodeAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = 'cash', 'expiration_date','code'
    list_display_links = 'cash',
    list_editable = 'expiration_date','code'
=======
    pass
>>>>>>> 2e567137b12a8e3fc6bf62255974ab8998a032a4


@admin.register(models.SpecificCash)
class SpecificCashAdmin(admin.ModelAdmin):
    pass
