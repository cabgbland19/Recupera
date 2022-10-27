from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from sqlalchemy import false
from django.utils import timezone
from datetime import datetime

class UserManager(BaseUserManager):
    def _create_user(self,document, username, name, password, is_superuser, **extra_fields):
        user = self.model(
            document=document,
            username = username,
            name = name,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, document,username, name, password=None, **extra_fields):
        return self._create_user(document,username, name, password, False, False, **extra_fields)

    def create_superuser(self,document ,username, name, password=None, **extra_fields):
        return self._create_user(document,username, name, password, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    document=models.IntegerField('Documento',default = 1,null = False)
    username = models.IntegerField('username',default = 1,null = False, unique=True)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    cost_center=models.IntegerField('Centro de costos',default = 1,null = False)
    campaign=models.CharField('Campaña', max_length = 255, blank = True, null = True )
    is_active = models.BooleanField(default = True)
    rol=models.CharField(max_length = 255, default = "backoffice")
    id_rol=models.IntegerField( default = 1)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['document','name','cost_center','campaign','id_rol','rol']

    def __str__(self):
        return f'{self.name}'


class RegistersUsers(models.Model):
    user=models.CharField(max_length = 255)
    state=models.CharField(max_length = 255)
    datetimes=models.DateTimeField()