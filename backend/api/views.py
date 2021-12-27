from django.http import HttpResponse

from .models import Painting, Creator, Depiction, Genre, Location, Material, Movement
from worker.tasks import import_from_paintings_interval, populate_database
from api.serializers import PaintingSerializer, CreatorSerializer, DepictionSerializer, GenreSerializer, LocationSerializer, MovementSerializer, MaterialSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'paintings': reverse('paintings-list', request=request, format=format),
        'creators': reverse('creators-list', request=request, format=format),
        'depicts': reverse('depicts-list', request=request, format=format),
        'genres': reverse('genres-list', request=request, format=format),
        'locations': reverse('locations-list', request=request, format=format),
        'movements': reverse('movements-list', request=request, format=format),
        'materials': reverse('materials-list', request=request, format=format)
    })

# def coucou(request):
#     # populate_database.s().delay()
#     import_from_paintings_interval(30, 0)
#     return HttpResponse('let\'s go')

class PaintingsSet(generics.ListAPIView):
    queryset = Painting.objects.with_picture().with_readable_name()
    serializer_class = PaintingSerializer

class PaintingDetail(generics.RetrieveAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer


class CreatorsSet(generics.ListAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class CreatorDetail(generics.RetrieveAPIView):
    serializer_class = CreatorSerializer
    queryset = Creator.objects.all()


class DepictsSet(generics.ListAPIView):
    queryset = Depiction.objects.all()
    serializer_class = DepictionSerializer

class DepictionDetail(generics.RetrieveAPIView):
    serializer_class = DepictionSerializer
    queryset = Depiction.objects.all()

class GenresSet(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(generics.RetrieveAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class LocationsSet(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class MaterialsSet(generics.ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MaterialDetail(generics.RetrieveAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()

class MovementsSet(generics.ListAPIView):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer

class MovementDetail(generics.RetrieveAPIView):
    serializer_class = MovementSerializer
    queryset = Movement.objects.all()