from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


UM = get_user_model()


class UMAdmin(UserAdmin):
    model = UM
    list_display = ["id", "username", "email", "date_of_birth"]
    fieldsets = [["Edit User Account", {"fields": ["email", "username", "first_name", "last_name", "date_of_birth", "password"]}]]
    add_fieldsets = [["Create Account", {"fields": ["email", "username", "first_name", "last_name", "date_of_birth", "password1", "password2"]}]]
    filter_horizontal = []
    list_filter = []
    ordering = ("email", )


admin.site.register(UM, UMAdmin)
