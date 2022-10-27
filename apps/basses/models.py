from datetime import date
from email.policy import default
from faulthandler import cancel_dump_traceback_later
from unittest.util import _MAX_LENGTH

from django.db import models
from datetime import datetime



class recoverBase(models.Model):
    document=models.IntegerField()
    name=models.CharField(max_length=255, default="user")
    numberOne=models.IntegerField()
    numberTwo=models.IntegerField()
    observation=models.CharField(max_length=400)
    line=models.CharField(max_length=255)
    account=models.IntegerField()
    gestor=models.CharField(max_length=255)
    date=models.DateField()
    is_active=models.BooleanField(default = False)


class finalBase(models.Model):
    document=models.IntegerField()
    name=models.CharField(max_length=255, default="user")
    numberOne=models.IntegerField()
    numberTwo=models.IntegerField()
    observation=models.CharField(max_length=400)
    line=models.CharField(max_length=255)
    account=models.IntegerField()
    gestor=models.CharField(max_length=255)
    date=models.DateField()
    newGestor=models.DateTimeField()


class Names(models.Model):
    document=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255, default="user")
    

class Rols(models.Model):
    id=models.IntegerField(primary_key=True)
    rol_name=models.CharField(max_length=255, default="ADMIN")
    spanish_name=models.CharField(max_length=255 ,default="ADMINISTRADOR")


class Campaign(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)