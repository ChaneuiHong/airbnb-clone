from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


# 기본 admin model로 models.Users를 등록
@admin.register(models.Users)
class CustomUserAdmin(UserAdmin):

    """Custom User Adimin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
