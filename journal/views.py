from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Journal, Volume
from .serializers import JournalSerializer, VolumeSerializer
from rest_framework import serializers, status


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add Journal': '/add_journal',
        'Add Volume': '/add_volume',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(api_urls)


@api_view(['POST'])
def add_journal(request):
    journal = JournalSerializer(data=request.data)

    # validating for already existing data
    if Journal.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This journal already exists')

    if journal.is_valid():
        journal.save()
        return Response(journal.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_journals(request):
    # checking for the parameters from the URL
    if request.query_params:
        journals = Journal.objects.filter(**request.query_params.dict())
    else:
        journals = Journal.objects.all()

    # if there is something in items else raise error
    if journals:
        serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_journal(request, pk):
    journal = Journal.objects.get(pk=pk)
    data = JournalSerializer(instance=journal, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_journal(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    journal.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def add_volume(request):
    volume = VolumeSerializer(data=request.data)

    # validating for already existing data
    if Volume.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This volume already exists')

    if volume.is_valid():
        volume.save()
        return Response(volume.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_volumes(request):
    # checking for the parameters from the URL
    if request.query_params:
        volumes = Volume.objects.filter(**request.query_params.dict())
    else:
        volumes = Volume.objects.all()

    # if there is something in items else raise error
    if volumes:
        serializer = VolumeSerializer(volumes, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_volume(request, pk):
    volume = Volume.objects.get(pk=pk)
    data = VolumeSerializer(instance=volume, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_volume(request, pk):
    volume = get_object_or_404(Volume, pk=pk)
    volume.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
