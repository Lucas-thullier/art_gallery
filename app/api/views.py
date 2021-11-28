from django import template
from django.template import context
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse

from .models import Artwork
from worker.tasks import fetch_data_from_quandl

class IndexView(generic.ListView):
    template_name = 'api/artworks/index.html'
    context_object_name = 'artworks'

    def get_queryset(self):
        return Artwork.objects.order_by('-created_at')[:5]

class DetailView(generic.DetailView):
    model = Artwork
    template_name = 'api/artworks/detail.html'

def coucou(request):
    fetch_data_from_quandl.s(database_code=1,dataset_code=1).delay()
        
    return HttpResponse("You're looking at question.")
