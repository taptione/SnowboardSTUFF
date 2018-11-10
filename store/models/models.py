from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from store.models.managers import UserManager
from rest_framework.authtoken.models import Token


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name',
                                  max_length=30, blank=False)
    last_name = models.CharField('last name',
                                 max_length=30, blank=False)
    phone = models.IntegerField('phone', blank=False)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'


class ExpiredToken(Token):
    modified = models.DateTimeField(auto_now=True)
    is_expired = models.BooleanField(default=False)

    class Meta:
        db_table = 'expire_token'
