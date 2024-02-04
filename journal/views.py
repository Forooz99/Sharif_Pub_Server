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
        journals = Journal.objects.all()
        if journals:
            serializer = JournalSerializer(journals, many=True)
            return Response(serializer.data, status=200, content_type='application/json')
        else:
            return Response(data="Cant Get Journals Details", status=400, content_type='application/json')

    def post(self, request):
        serializer = JournalSerializer(data=request.data)
        if not request.data:
            return Response(data="Error Message: Empty Body", status=400, content_type='application/json')
        elif Journal.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This journal already exists')

        if serializer.is_valid():
            serializer.save()
            return Response(data="New Journal Added Successfully", status=201, content_type='application/json')
        return Response(data="Cant Add New Journal", status=400, content_type='application/json')


class JournalByIdAPI(APIView):

    def get_journal(self, pk):
        try:
            return Journal.objects.get(pk=pk)
        except Journal.DoesNotExist:
            return Response(status=400, content_type='application/json')

    def get(self, request, pk):
        journal = self.get_journal(pk)
        serializer = JournalSerializer(journal)
        return Response(serializer.data)

    def put(self, request, pk):
        journal = self.get_journal(pk)
        serializer = JournalSerializer(instance=journal, data=request.data, content_type='application/json')

        if serializer.is_valid():
            serializer.save()
            return Response(data="Journal Is Updated Successfully", status=200, content_type='application/json')
        else:
            return Response(data="Cant Update Journal", status=400, content_type='application/json')

    def delete(self, request, pk):
        journal = self.get_journal(pk)
        journal.delete()
        return Response(data="Journal Is Deleted Successfully", status=202, content_type='application/json')


class VolumesAPI(APIView):

    def get(self, request):
        volumes = Volume.objects.all()
        if volumes:
            serializer = VolumeSerializer(volumes, many=True)
            return Response(serializer.data, status=200, content_type='application/json')
        else:
            return Response(status=400, content_type='application/json')

    def post(self, request):
        serializer = VolumeSerializer(data=request.data)

        if not request.data:
            return Response(data="Error Message: Empty Body", status=400, content_type='application/json')

        if Volume.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This volume already exists')

        if serializer.is_valid():
            serializer.save()
            return Response(data="New Volume Added Successfully", status=201, content_type='application/json')
        return Response(data="Cant Add New Volume", status=400, content_type='application/json')


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
        serializer = VolumeSerializer(instance=volume, data=request.data, content_type='application/json')

        if serializer.is_valid():
            serializer.save()
            return Response(data="Volume Is Updated Successfully", status=200, content_type='application/json')
        else:
            return Response(data="Cant Update Volume", status=400, content_type='application/json')

    def delete(self, request, pk):
        volume = self.get_volume(pk)
        volume.delete()
        return Response(data="Volume Is Deleted Successfully", status=202, content_type='application/json')
