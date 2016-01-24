from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from datetime import date


#CharField (and its subclasses) require a max_length argument which specifies the size of the VARCHAR database field used to store the data
#the primary auto keys in ldm are not mentioned in models because we use django id which is an auto key itself

class Parent(AbstractBaseUser):
    account_no = models.ForeignKey(User, unique=True)
    national_id = models.IntegerField(null=False, primary_key=True)
    tell_number = models.IntegerField()


class Student(AbstractBaseUser):
    account_no = models.ForeignKey(User, unique=True)#to use django default auto id
    national_id = models.IntegerField(null=False, primary_key=True)
    parent_na_id = models.ForeignKey(Parent, to_field='national_id')#to use an specific pi
    total_average = models.FloatField()
    registration_date = models.DateField(default=date.today())


class Employee(AbstractBaseUser):
    account_no = models.ForeignKey(User, unique=True)
    national_id = models.IntegerField(null=False, primary_key=True)

class Teacher(AbstractBaseUser):
    account_no = models.ForeignKey(User, unique=True)
    national_id = models.IntegerField(null=False, primary_key=True)


class Manager(AbstractBaseUser):
    account_no = models.ForeignKey(User, unique=True)
    national_id = models.IntegerField(null=False, primary_key=True)


class Course(models.Model):
    name = models.CharField(null=False, max_length=50)


class Suggested_course(models.Model):
    term_nu = models.IntegerField(null=False)
    teacher = models.ForeignKey(Teacher, to_field='national_id')
    exam_date = models.DateField()
    course_no = models.ForeignKey(Course)


class Registered_course(models.Model):
    student = models.ForeignKey(Student, to_field='national_id')
    suggested_cou = models.ForeignKey(Suggested_course)
    term_no = models.IntegerField(null=False)
    top_grade = models.IntegerField()
    second_top_grade = models.IntegerField()


class Practice(models.Model):
    register_cou = models.ForeignKey(Registered_course)
    grade = models.FloatField()
    due_date = models.DateField(default=date.today())


class result(models.Model):
    term_no = models.IntegerField(primary_key=True, null=False)
    term_score = models.FloatField() #said average in ldm
    student_no = models.ForeignKey(Student, to_field='national_id')

    class Meta:
        unique_together = (("term_no", "student_no"),)#is this working?we needed both as a pi
