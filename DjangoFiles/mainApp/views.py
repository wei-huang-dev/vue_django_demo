from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Book, Author, Genre, Language 
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def index(request):
    return HttpResponse("This first view is working as inteded.")

@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def book_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try: 
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)



class BookViewSet(viewsets.ModelViewSet):
    """
        The viewset for the Books table. If no 
        url parameters are passed, it gets all the objects. 
        If the langID is set in the url then it gets the objects 
        with the matching language
    """
    # determines which serializer to be used
    serializer_class = BookSerializer

    # ensures that users are logged in to access this API
    permission_classes = [IsAuthenticated]

    # overrides the get_queryset method. This is where the logic for 
    # langID is defined
    def get_queryset(self):
        queryset = Book.objects.all()
        languageId = self.request.query_params.get('langID', None)
        if languageId is not None:
            queryset = queryset.filter(language = languageId)
        return queryset


    def list(self, request):
        serializer = BookSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)