from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone_number", "created_at")
    search_fields = ("full_name", "email", "phone_number")
    list_filter = ("created_at",)
    ordering = ("-created_at",)  # Latest messages first
