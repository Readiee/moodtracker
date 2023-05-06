from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
import datetime
from .managers import UserManager
import uuid
from shortuuid.django_fields import ShortUUIDField


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    login = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    date_create = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    unique_id = ShortUUIDField(
        length=5,
        max_length=5,
        alphabet="123456789",
        unique=True
    )
    avatar = models.FileField(upload_to='user/', default='user/default_image.png')

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name


class Tracker(models.Model):
    image = models.FileField(upload_to='tracker/')
    mood = models.CharField(max_length=255, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Friend(models.Model):
    class Meta:
        unique_together = ('user', 'friend')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')
