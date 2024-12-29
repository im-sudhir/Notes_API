from django.shortcuts import render
from .serializers import NotesSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Notes

# Create your views here.

class NotesListCreateView(ListCreateAPIView):
    serializer_class= NotesSerializer
    queryset= Notes.objects.all()

class NotesDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class=NotesSerializer
    queryset=Notes.objects.all()