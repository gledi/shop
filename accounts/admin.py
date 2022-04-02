from django.contrib import admin

from accounts.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["user", "is_manager"]
