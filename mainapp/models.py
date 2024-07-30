from django.db import models

# Create your models here.
class Patient(models.Model):
    pprofilepic=models.FileField(max_length=500)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    emailaddress=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=10)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    pincode=models.CharField(max_length=30)
class Doctor(models.Model):
    dprofilepic=models.FileField(max_length=500)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    emailaddress=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=10)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    pincode=models.CharField(max_length=30)
class Login(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=30)
    usertype=models.CharField(max_length=30)