from uuid import uuid4
from django.db import models
import uuid
from django.contrib import admin
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.admin import UserAdmin
# Create your models here.

admin.site.unregister(User)

@admin.register(User)
class CustomUSerAdmin(UserAdmin):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return (self.user.first_name +' ' + self.user.last_name)