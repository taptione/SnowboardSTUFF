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


class Brand(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Brand name'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'brands'
        verbose_name = 'Brand'


class Category(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Category'
    )
    parent_category = models.ForeignKey(
        'Category',
        on_delete=None,
        verbose_name='Parent category'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'


class Item(models.Model):
     mame = models.CharField(
        max_length=256,
        verbose_name='Item name'
    )
    gender = models.ForeignKey(
        'Gender',
        on_delete=None,
        null=True,
        verbose_name='Gender',
        related_name='gender_set'
    )
    size = models.ManyToManyField(
        'Size',
        null=True,
        verbose_name='Size',
        related_name='size_set'
    )
    quantity = models.CharField(
        max_length=4,
        verbose_name='Quantity'
    )
    price = models.IntegerField(
        default=0,
        verbose_name='Price'
    )
    status = models.ForeignKey(
        'ItemStatus',
        on_delete=None,
        verbose_name='Item status',
        related_name='item_status_set'
    )
    description = models.TextField(
        verbose_name='Description'
    )
    image = models.ForeignKey(
        'Image',
        on_delete=None,
        verbose_name='Image',
        related_name='image_set'
    )

    def __str__(self):
        return self.mame, self.gender, self.size, self.price, self.status

    class Meta:
        db_table = 'items'
        verbose_name = 'Item'


class Size(models.Model):
    value = models.CharField(
        max_length=32,
        verbose_name='Value'
    )
    unit = models.CharField(
        max_length=32,
        verbose_name='Units'
    )

    def __str__(self):
        return self.value, self.unit

    class Meta:
        db_table = 'sizes'
        verbose_name = 'Size'

class Gender(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Gender'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'genders'
        verbose_name = 'Gender'

class ItemStatus(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Item status'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'item_statuses'
        verbose_name = 'Item status'


class Image(models.Model):
    name = models.CharField(max_length=128)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'images'
        verbose_name = 'Image'
