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
        verbose_name=u'Назва бренду'
    )

    class Meta:
        db_table = 'brand'
        verbose_name = u'Бренд'
        verbose_name_plural = u'Бренди'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name=u'Назва категорії'
    )
    parent_category = models.ForeignKey(
        'Category',
        on_delete=None,
        null=True,
        verbose_name=u'Основна категорія'
    )

    class Meta:
        db_table = 'category'
        verbose_name = u'Категорія'
        verbose_name_plural = u'Категорії'

    def __str__(self):
        return self.name


class Item(models.Model):
    class Meta:
        db_table = 'item'
        verbose_name = u'Товар'
        verbose_name_plural = u'Товари'

    mame = models.CharField(
        max_length=256,
        verbose_name=u'Назва товару'
    )
    gender = models.ForeignKey(
        'Gender',
        on_delete=None,
        blank=True,
        null=True,
        verbose_name=u'Стать, вік'
    )
    size = models.ManyToManyField(
        'Size',
        null=True,
        blank=True,
        verbose_name=u'Розмір'
    )
    quantity = models.CharField(
        max_length=4,
        blank=True,
        verbose_name=u'Кількість одиниць'
    )
    price = models.IntegerField(
        default=0,
        verbose_name=u'Ціна'
    )
    status = models.ForeignKey(
        'ItemStatus',
        on_delete=None,
        verbose_name=u'Наявність'
    )

    def __str__(self):
        return self.mame, self.gender, self.size, self.price, self.status


class Size(models.Model):
    value = models.CharField(
        max_length=32,
        verbose_name=u'Значення'
    )
    unit = models.CharField(
        max_length=32,
        verbose_name=u'Одиниці вимірювання'
    )

    class Meta:
        db_table = 'size'
        verbose_name = u'Розмір'

    def __str__(self):
        return self.value, self.unit


class Gender(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name=u'Стать'
    )

    class Meta:
        db_table = 'gender'
        verbose_name = u'Стать'

    def __str__(self):
        return self.name


class ItemStatus(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name=u'Наявність'
    )

    class Meta:
        db_table = 'item_status'

    def __str__(self):
        return self.name


class Image(models.Model):
    image_name = models.CharField(max_length=128)
    is_main = models.BooleanField(default=False)

    class Meta:
        db_table = 'image'
