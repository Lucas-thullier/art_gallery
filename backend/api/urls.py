from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', views.api_root),

    path('painting/coucou/', views.coucou, name='coucou'),
    path('fulltext-search/', views.fulltext_search, name='fulltext_search'),

    path('kill-tasks/', views.purgeWaitingAndReservedTasks, name='purgeTasks'),

    path('painting/all/', views.PaintingsSet.as_view(), name='paintings-list'),
    path('painting/<int:pk>/', views.PaintingDetail.as_view(),
         name='painting-detail'),

    path('creator/all/', views.CreatorsSet.as_view(), name='creators-list'),
    path('creator/<int:pk>/', views.CreatorDetail.as_view(),  name='creator-detail'),

    path('creator/<int:pk>/detailed', views.creator_details,  name='creator-detail-full'),


    path('depiction/all/', views.DepictsSet.as_view(), name='depicts-list'),
    path('depiction/<int:pk>/', views.DepictionDetail.as_view(),
         name='depiction-detail'),

    path('genre/all/', views.GenresSet.as_view(), name='genres-list'),
    path('genre/<int:pk>/', views.GenreDetail.as_view(),  name='genre-detail'),

    path('location/all/', views.LocationsSet.as_view(), name='locations-list'),
    path('location/<int:pk>/', views.LocationDetail.as_view(),
         name='location-detail'),

    path('material/all/', views.MaterialsSet.as_view(), name='materials-list'),
    path('material/<int:pk>/', views.MaterialDetail.as_view(),
         name='material-detail'),

    path('movement/all/', views.MovementsSet.as_view(), name='movements-list'),
    path('movement/<int:pk>/', views.MovementDetail.as_view(),
         name='movement-detail'),
])
