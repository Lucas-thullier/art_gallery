from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'gallery'

urlpatterns = [
    path('painting/coucou/', views.coucou, name='coucou'),
    path('painting/all/', views.PaintingsSet.as_view()),
    path('painting/<int:pk>/', views.PaintingDetail.as_view()),
]
