from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reader, Publisher
from .serializers import ReaderSerializer, PublisherSerializer
from rest_framework import serializers, status


class ReaderAPIView(APIView):
    queryset = Reader.objects.all()
    serializer = ReaderSerializer()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        self.serializer = ReaderSerializer(data=data)

        if self.serializer.is_valid():
            self.serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.serializer = ReaderSerializer(instance, data=request.data, partial=True)
            if self.serializer.is_valid():
                self.serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            instance.delete()
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class PublisherAPIView(APIView):
    queryset = Publisher.objects.all()
    serializer = PublisherSerializer()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        self.serializer = PublisherSerializer(data=data)
        if self.serializer.is_valid():
            self.serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.serializer = PublisherSerializer(instance, data=request.data, partial=True)
            if self.serializer.is_valid():
                self.serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            instance.delete()
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
