from django import template
from django.template import context
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Painting
from .repository import with_readable_name, with_picture
from worker.tasks import import_from_paintings_interval, populate_database


class IndexView(generic.ListView):
    template_name = 'paintings/index.html'
    context_object_name = 'paintings'

    def get_queryset(self):
        base_manager = Painting.objects
        paintings_query = with_readable_name(base_manager)
        paintings_query = with_picture(paintings_query)

        return paintings_query.order_by('-created_at')[:5]


class DetailView(generic.DetailView):
    model = Painting
    template_name = 'paintings/detail.html'


def coucou(request):
    # t = import_from_paintings_interval(20, 20)
    populate_database.s().delay()
    # return HttpResponse(t)
    return HttpResponse('let\'s go')
    # return HttpResponse('cc')
