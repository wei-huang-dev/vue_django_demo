from django.db import models
#from django import forms

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    





