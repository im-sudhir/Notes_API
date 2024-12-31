from django.urls import path
from .views import NotesListCreateView, NotesDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("notes", NotesListCreateView.as_view(), name="notes"),
    path('notes/<int:pk>',NotesDetailView.as_view(), name='notes-detail'),
]

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
