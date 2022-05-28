from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    repassword=models.CharField(max_length=30)

class sell_property(models.Model):
    id=models.AutoField(primary_key=True)
    Property_Name=models.CharField(max_length=30)
    Location=models.CharField(max_length=30)
    Price=models.CharField(max_length=30)
    Area=models.CharField(max_length=30)
    Property_Description=models.CharField(max_length=300)
    Status=models.CharField(max_length=30)
    Bedrooms=models.CharField(max_length=30)
    Bathrooms=models.CharField(max_length=30)
    Garages=models.CharField(max_length=30)
    rent_or_sell=models.CharField(max_length=30)
    facilities=models.CharField(max_length=30)
    photo = models.ImageField(upload_to="userimages") 

class sell_property1(models.Model):
    id=models.AutoField(primary_key=True)
    Property_Name=models.CharField(max_length=30)
    photo1 = models.ImageField(upload_to="userimages") 
    photo2 = models.ImageField(upload_to="userimages") 
    photo3 = models.ImageField(upload_to="userimages") 

