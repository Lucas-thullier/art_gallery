from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    path('painting/list', views.IndexView.as_view(), name='index'),
    path('painting/<int:pk>/', views.DetailView.as_view(), name='detail'),
    
    path('painting/coucou', views.coucou, name='coucou'),
    path('painting/test', views.test, name='test'),
]
