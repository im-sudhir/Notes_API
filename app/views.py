from django.shortcuts import render
from .serializers import NotesSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Notes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class NotesListCreateView(ListCreateAPIView):
    serializer_class= NotesSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return Notes.objects.filter(author=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class NotesDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class=NotesSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return Notes.objects.filter(author=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save()
