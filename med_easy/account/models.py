from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.validators import RegexValidator

class User(AbstractUser):
	is_patient = models.BooleanField('patient status', default=True)
	phone_number = models.CharField(max_length=17, blank=False)

class Doctor(models.Model):
	user_id=models.OneToOneField(User, on_delete=models.CASCADE)
	speciality=models.CharField(max_length=20)
	city=models.CharField(max_length=15)
	hospital=models.CharField(max_length=100)
	avatar=models.ImageField(upload_to='doctor/avatar')


class Patient(models.Model):
	user_id=models.OneToOneField(User, on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True, verbose_name="DOB")
	blood_group=models.CharField(max_length=5)
	address=models.CharField(max_length=200)
	height=models.PositiveIntegerField(null=True, blank=True)
	weight=models.PositiveIntegerField(null=True, blank=True)
	avatar=models.ImageField(upload_to='patient/avatar')

class History(models.Model):
	user_id=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
	date_of_issue=models.DateTimeField('last followed date')
	symptom_text=models.CharField(max_length=100, blank=True)
	description=models.CharField(max_length=300)
	height=models.PositiveIntegerField(null=True, blank=True)
	weight=models.PositiveIntegerField(null=True, blank=True)

class Medicine(models.Model):
	history_id=models.ForeignKey(History, on_delete=models.SET_NULL, null=True)
	medicines=models.CharField(max_length=100)

class OtptStorage(models.Model):
	date_of_issue=models.DateTimeField('last followed date')
	phone_number=models.CharField(max_length=17)
	otp=models.PositiveIntegerField(null=False, blank=False)