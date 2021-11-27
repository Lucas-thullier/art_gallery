from django import template
from django.template import context
from django.views import generic
from django.shortcuts import render

from .models import Artwork

class IndexView(generic.ListView):
    template_name = 'gallery_backend/artworks/index.html'
    context_object_name = 'artworks'

    def get_queryset(self):
        return Artwork.objects.order_by('-created_at')[:5]

class DetailView(generic.DetailView):
    model = Artwork
    template_name = 'gallery_backend/artworks/detail.html'
