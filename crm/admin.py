from django.contrib import admin
from .models import UserForm


@admin.register(UserForm)
class UserFormAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")
    search_fields = ("name", "email")
