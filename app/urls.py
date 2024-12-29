from django.urls import path
from .views import NotesListCreateView, NotesDetailView

urlpatterns = [
    path("notes", NotesListCreateView.as_view(), name="notes"),
    path('notes/<int:pk>',NotesDetailView.as_view(), name='notes-detail'),
]
