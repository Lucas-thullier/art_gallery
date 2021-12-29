import json
from django.http import HttpResponse

from .models import Painting, Creator, Depiction, Genre, Location, Material, Movement
from worker.tasks import import_from_paintings_interval, populate_database
from api.serializers import PaintingSerializer, CreatorSerializer, DepictionSerializer, GenreSerializer, LocationSerializer, MovementSerializer, MaterialSerializer, SimplePaintingSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from worker.worker import app


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


def coucou(request):
    populate_database.s().delay()
    # import_from_paintings_interval(5, 0)
    return HttpResponse('let\'s go')


def purgeWaitingAndReservedTasks(request):
    app.control.purge()

    inspector = app.control.inspect()
    jobs = inspector.active()
    for hostname in jobs:
        tasks = jobs[hostname]
        for task in tasks:
            app.control.revoke(task['id'], terminate=True)

    jobs = inspector.reserved()
    for hostname in jobs:
        tasks = jobs[hostname]
        for task in tasks:
            app.control.revoke(task['id'], terminate=True)

    return HttpResponse(print('ok'))


class PaintingsSet(generics.ListAPIView):
    queryset = Painting.objects.with_picture().with_readable_name()
    serializer_class = SimplePaintingSerializer


class PaintingDetail(generics.RetrieveAPIView):
    queryset = Painting.objects.prefetch_related(
        'creators',
        'depicts',
        'genres',
        'locations',
        'materials',
        'movements'
    ).all()
    serializer_class = PaintingSerializer


class CreatorsSet(generics.ListAPIView):
    queryset = Creator.objects.prefetch_related('paintings').all()
    serializer_class = CreatorSerializer
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class CreatorDetail(generics.RetrieveAPIView):
    queryset = Creator.objects.prefetch_related('paintings').all()
    serializer_class = CreatorSerializer


class DepictsSet(generics.ListAPIView):
    queryset = Depiction.objects.prefetch_related('paintings').all()
    serializer_class = DepictionSerializer


class DepictionDetail(generics.RetrieveAPIView):
    queryset = Depiction.objects.prefetch_related('paintings').all()
    serializer_class = DepictionSerializer


class GenresSet(generics.ListAPIView):
    queryset = Genre.objects.prefetch_related('paintings').all()
    serializer_class = GenreSerializer


class GenreDetail(generics.RetrieveAPIView):
    queryset = Genre.objects.prefetch_related('paintings').all()
    serializer_class = GenreSerializer


class LocationsSet(generics.ListAPIView):
    queryset = Location.objects.prefetch_related('paintings').all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveAPIView):
    queryset = Location.objects.prefetch_related('paintings').all()
    serializer_class = LocationSerializer


class MaterialsSet(generics.ListAPIView):
    queryset = Material.objects.prefetch_related('paintings').all()
    serializer_class = MaterialSerializer


class MaterialDetail(generics.RetrieveAPIView):
    queryset = Material.objects.prefetch_related('paintings').all()
    serializer_class = MaterialSerializer


class MovementsSet(generics.ListAPIView):
    queryset = Movement.objects.prefetch_related('paintings').all()
    serializer_class = MovementSerializer


class MovementDetail(generics.RetrieveAPIView):
    queryset = Movement.objects.prefetch_related('paintings').all()
    serializer_class = MovementSerializer
