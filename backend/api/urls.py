from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    path('painting/list', views.IndexView.as_view(), name='index'),
    # path('painting/<int:pk>/', views.DetailView.as_view(), name='detail'),
    
    path('painting/coucou', views.coucou, name='coucou'),
    path('painting/test', views.test, name='test'),

    path('painting/all', views.get_viewable_paintings, name='all_paintings'),
    path('painting/<int:painting_id>/', views.get_painting_by_id, name='painting_by_id'),
]
