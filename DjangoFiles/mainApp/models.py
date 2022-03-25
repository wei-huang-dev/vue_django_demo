from django.db import models
#from django import forms

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
    def __str__(self):
        return "Pizza " + str(self.id)
