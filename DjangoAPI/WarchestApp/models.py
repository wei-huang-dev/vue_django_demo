from django.db import models

# Create your models here.

class WarchestData(models.Model):
    Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    Field1 = models.CharField(max_length=50)
    Field2 = models.CharField(max_length=50)
    Field3 = models.CharField(max_length=50)
    Field4 = models.CharField(max_length=50)
    Field5 = models.CharField(max_length=50)
    Date = models.DateField()
    photoFileName = models.CharField(max_length=50, default="")

class UserData(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    
