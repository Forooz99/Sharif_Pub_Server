from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Journal, Volume
from .serializers import JournalSerializer, VolumeSerializer
from rest_framework import serializers, status


@api_view(['GET'])
def view_journals(request):
    journals = Journal.objects.all()
    if journals:
        serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_journal(request, pk):
    try:
        journal = Journal.objects.get(pk=pk)
    except Journal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = JournalSerializer(journal, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_journal(request):
    journal = JournalSerializer(data=request.data)

    if Journal.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This journal already exists')

    if journal.is_valid():
        journal.save()
        return Response(journal.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
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
    try:
        journal = Journal.objects.get(pk=pk)
    except Journal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    journal.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def view_volumes(request):
    volumes = Volume.objects.all()
    if volumes:
        serializer = VolumeSerializer(volumes, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_volume(request, pk):
    try:
        volume = Volume.objects.get(pk=pk)
    except Volume.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = VolumeSerializer(volume, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_volume(request):
    volume = VolumeSerializer(data=request.data)

    if Volume.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This volume already exists')

    if volume.is_valid():
        volume.save()
        return Response(volume.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
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
    try:
        volume = Volume.objects.get(pk=pk)
    except Volume.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    volume.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
