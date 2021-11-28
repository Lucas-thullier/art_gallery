from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    path('artworks/list', views.IndexView.as_view(), name='index'),
    path('artworks/coucou', views.coucou, name='coucou'),
    path('artworks/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
