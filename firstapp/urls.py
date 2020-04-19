from django.urls import path
from . import views

urlpatterns = [
    path('api/human/', views.humans.as_view(), name='humans'),
    path('api/human/<int:id>', views.human.as_view(), name='human'),
]