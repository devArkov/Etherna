from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserInterest(models.Model):
    interest = models.CharField(max_length=64, unique=True)
    normalized = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.interest


class UserPersona(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    # Owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Details
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null=True)
    interests = models.ManyToManyField(UserInterest, blank=True)
    # Settings
    is_full_name_displayed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username.capitalize()
