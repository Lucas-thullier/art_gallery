from django.http import HttpResponse
from .models import Painting
from worker.tasks import populate_database
from api.serializers import PaintingSerializer
from rest_framework import generics


def coucou(request):
    populate_database.s().delay()
    return HttpResponse('let\'s go')

class PaintingsSet(generics.ListAPIView):
    queryset = Painting.objects.with_picture().with_readable_name()
    serializer_class = PaintingSerializer

class PaintingDetail(generics.RetrieveAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer