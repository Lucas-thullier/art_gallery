from django.http import HttpResponse

from .models import Painting, Creator
from worker.tasks import populate_database
from api.serializers import PaintingSerializer, CreatorSerializer
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

class CreatorsSet(generics.ListAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CreatorDetail(generics.RetrieveAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer