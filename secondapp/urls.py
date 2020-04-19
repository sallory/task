from django.urls import path
from . import views

urlpatterns = [
    path('api/match/', views.matches.as_view(), name='matches'),
    path('api/match/<int:human_id>', views.match.as_view(), name='match'),
]