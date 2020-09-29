from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from .permissions import ReadOnly

class PostBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RetrieveBook(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (ReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer