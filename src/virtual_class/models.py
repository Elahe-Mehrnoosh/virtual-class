from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

class Parent(models.Model):
    user = models.ForeignKey(User, unique=True)
    nationalid = models.IntegerField(null=False, primary_key=True)


class Student(AbstractBaseUser):
    user = models.ForeignKey(User, unique=True)
    national_id = models.IntegerField(null=False, primary_key=True)
    parent_na_id = models.ForeignKey(Parent)


class Employee(AbstractBaseUser):
    user = models.ForeignKey(User, unique=True)
    national_id = models.IntegerField(null=False, primary_key=True)

class Teacher(AbstractBaseUser):
    user = models.ForeignKey(User, unique=True)
    national_id = models.IntegerField(null=False, primary_key=True)


class Manager(AbstractBaseUser):
    user = models.ForeignKey(User, unique=True)
    national_id = models.IntegerField(null=False, primary_key=True)

