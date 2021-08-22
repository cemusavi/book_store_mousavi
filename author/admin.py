from django.contrib import admin
from . import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
