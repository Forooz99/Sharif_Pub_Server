from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Journal, Volume
from .serializers import JournalSerializer, VolumeSerializer
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class JournalsAPI(APIView):

    def get(self, request):
        journals = Journal.objects.all()  # Getting all values
        if journals:
            serializer = JournalSerializer(journals, many=True)
            return Response(serializer.data, status=200)
        else:
            return Response(status=400)

    def post(self, request):
        serializer = JournalSerializer(data=request.data)  # data passed in the body

        if Journal.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This journal already exists')

        if serializer.is_valid():
            serializer.save()  # post request
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)  # if error


class JournalByIdAPI(APIView):

    def get_journal(self, pk):
        try:
            return Journal.objects.get(pk=pk)
        except Journal.DoesNotExist:
            return Response(status=400)

    def get(self, request, pk):
        journal = self.get_journal(pk)
        serializer = JournalSerializer(journal)
        return Response(serializer.data)

    def put(self, request, pk):
        journal = self.get_journal(pk)
        serializer = JournalSerializer(instance=journal, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        journal = self.get_journal(pk)
        serializer = JournalSerializer(instance=journal)
        journal.delete()
        return Response(serializer.data, status=202)


class VolumesAPI(APIView):

    def get(self, request):
        volumes = Volume.objects.all()
        if volumes:
            serializer = VolumeSerializer(volumes, many=True)
            return Response(serializer.data, status=200)
        else:
            return Response(status=400)

    def post(self, request):
        serializer = VolumeSerializer(data=request.data)

        if Volume.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This volume already exists')

        if serializer.is_valid():
            serializer.save()  # post request
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class VolumeByIdAPI(APIView):

    def get_volume(self, pk):
        try:
            return Volume.objects.get(pk=pk)
        except Volume.DoesNotExist:
            return Response(status=400)

    def get(self, request, pk):
        volume = self.get_volume(pk)
        serializer = VolumeSerializer(volume)
        return Response(serializer.data)

    def put(self, request, pk):
        volume = self.get_volume(pk)
        serializer = VolumeSerializer(instance=volume, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        volume = self.get_volume(pk)
        serializer = VolumeSerializer(instance=volume)
        volume.delete()
        return Response(serializer.data, status=202)
