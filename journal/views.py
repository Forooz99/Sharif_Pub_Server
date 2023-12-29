from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Journal, Volume
from .serializers import JournalSerializer, VolumeSerializer
from rest_framework import serializers, status


class VolumeListApiView(APIView):
    def get(self, request, *args, **kwargs):
        volumes = Volume.objects.all()
        serializer = VolumeSerializer(volumes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = VolumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VolumeDetailApiView(APIView):
    def get_object(self, volume_id):
        try:
            return Volume.objects.get(id=volume_id)
        except Volume.DoesNotExist:
            return None

    def get(self, request, volume_id, *args, **kwargs):
        volume_instance = self.get_object(volume_id)
        if not volume_instance:
            return Response(
                {"res": "Object with volume id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = VolumeSerializer(volume_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, volume_id, *args, **kwargs):
        volume_instance = self.get_object(volume_id, request.user.id)
        if not volume_instance:
            return Response(
                {"res": "Object with volume id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = VolumeSerializer(instance=volume_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, volume_id, *args, **kwargs):
        todo_instance = self.get_object(volume_id, request.user.id)
        if not volume_id:
            return Response(
                {"res": "Object with volume id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        volume_id.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class JournalListApiView(APIView):
    def get(self, request, *args, **kwargs):
        journals = Journal.objects.all()
        serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JournalDetailApiView(APIView):
    def get_object(self, journal_id):
        try:
            return Journal.objects.get(id=journal_id)
        except Volume.DoesNotExist:
            return None

    def get(self, request, journal_id, *args, **kwargs):
        journal_instance = self.get_object(journal_id)
        if not journal_instance:
            return Response(
                {"res": "Object with volume id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = JournalSerializer(journal_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, journal_id, *args, **kwargs):
        journal_instance = self.get_object(journal_id)
        if not journal_instance:
            return Response(
                {"res": "Object with volume id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = JournalSerializer(instance=journal_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, journal_id, *args, **kwargs):
        journal_instance = self.get_object(journal_id)
        if not journal_instance:
            return Response(
                {"res": "Object with volume id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        journal_id.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )