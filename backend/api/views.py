import json
from django.http import HttpResponse, JsonResponse
from django.db.models import Count
from django.contrib.postgres.search import SearchVector, SearchQuery

from .models import Painting, Creator, Depiction, Genre, Location, Material, Movement
from worker.tasks import import_from_paintings_interval, populate_database
from api.serializers.depth_one import PaintingSerializer, CreatorSerializer, DepictionSerializer, GenreSerializer, LocationSerializer, MovementSerializer, MaterialSerializer
from api.serializers.simple import SimplePaintingSerializer, SimpleCreatorSerializer, SimpleDepictionSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
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
    # populate_database.s().delay()
    # import_from_paintings_interval(5, 0)

    Painting.objects.all().values('creators').annotate(
        total=Count('creators')).order_by('-total')
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
    queryset = Creator.objects.with_picture().with_readable_name().order_by('name')
    serializer_class = CreatorSerializer


class CreatorDetail(generics.RetrieveAPIView):
    queryset = Creator.objects.all()
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


def creator_details(request, pk):
    depicts_details = get_creator_details_from_paintings(
        Depiction, 'depicts', pk)
    movements_details = get_creator_details_from_paintings(
        Movement, 'movements', pk)
    materials_details = get_creator_details_from_paintings(
        Material, 'materials', pk)

    details = {
        'depicts': depicts_details,
        'movements': movements_details,
        'materials': materials_details
    }

    return JsonResponse(details, safe=False)


def get_creator_details_from_paintings(class_wanted, class_name, creator_id):
    creator = Creator.objects.prefetch_related('paintings').get(id=creator_id)

    paintings = creator.paintings.prefetch_related(class_name).all()

    relation_details = class_wanted.objects.filter(paintings__in=paintings).values(
        'id', 'name').annotate(total=Count('name')).order_by('-total')

    return list(relation_details)


def fulltext_search(request):
    user_search = request.GET.get("search")
    user_search = SearchQuery(user_search)

    paintings = Painting.objects.annotate(
        search=SearchVector('name')).filter(search=user_search)[:5]

    creators = Creator.objects.annotate(
        search=SearchVector('name')).filter(search=user_search)[:5]

    depicts = Depiction.objects.annotate(
        search=SearchVector('name')).filter(search=user_search)[:5]

    search_return = {
        'paintings': SimplePaintingSerializer(
            paintings,
            context={'request': request},
            many=True
        ).data,
        'creators': SimpleCreatorSerializer(
            creators,
            context={'request': request},
            many=True
        ).data,
        'depicts': SimpleDepictionSerializer(
            depicts,
            context={'request': request},
            many=True
        ).data,
    }

    return JsonResponse(search_return, safe=False)
