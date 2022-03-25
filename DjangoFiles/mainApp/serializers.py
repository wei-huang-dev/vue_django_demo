from rest_framework import serializers
from .models import Author, Book, Genre, Language

class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'language']

