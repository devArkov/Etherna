from django.contrib import admin
from .models import UserProfile, UserPersona, UserInterest


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(UserPersona)
class UserPersonaAdmin(admin.ModelAdmin):
    pass


@admin.register(UserInterest)
class UserInterestAdmin(admin.ModelAdmin):
    pass
