from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reader, Publisher
from .serializers import ReaderSerializer, PublisherSerializer
from rest_framework import serializers, status
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def signup(request):
    if not request.data:
        return Response(data="Error Message: Empty Body", status=400, content_type='application/json')

    if request.data.get('type') == 'READER':
        reader = ReaderSerializer(data=request.data)
        if Reader.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This reader already exists')

        if reader.is_valid():
            reader.save()
            return Response(data="New Reader Added Successfully", status=201, content_type='application/json')
        else:
            return Response(data="Error Message: Bad Request", status=400, content_type='application/json')
    elif request.data.get('type') == 'PUBLISHER':
        publisher = PublisherSerializer(data=request.data)
        if Publisher.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This publisher already exists')

        if publisher.is_valid():
            publisher.save()
            return Response(data="New Publisher Added Successfully", status=201, content_type='application/json')
        else:
            return Response(data="Error Message: Bad Request", status=400, content_type='application/json')
    else:
        return Response(data="Error Message: Bad Request", status=400, content_type='application/json')


@api_view(['POST'])
def login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return Response(data="Successful Login", status=200, content_type='application/json')


@api_view(['POST'])
def logout(request):
    logout(request)
    return redirect('home')


class ReadersAPI(APIView):

    def get(self, request):
        readers = Reader.objects.all()
        if readers:
            serializer = ReaderSerializer(readers, many=True)
            return Response(serializer.data, status=200, content_type='application/json')
        else:
            return Response(data="Cant Get Readers Details", status=400, content_type='application/json')

    def post(self, request):
        serializer = ReaderSerializer(data=request.data)

        if not request.data:
            return Response(data="Error Message: Empty Body", status=400, content_type='application/json')
        elif Reader.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This Reader Already Exists')

        if serializer.is_valid():
            serializer.save()
            return Response(data="New Reader Added Successfully", status=201, content_type='application/json')
        return Response(data="Cant Add New Reader", status=400, content_type='application/json')


class ReaderByIdAPI(APIView):

    def get_reader(self, pk):
        try:
            return Reader.objects.get(pk=pk)
        except Reader.DoesNotExist:
            return Response(status=400, content_type='application/json')

    def get(self, request, pk):
        reader = self.get_reader(pk)
        serializer = ReaderSerializer(reader)
        return Response(serializer.data)

    def put(self, request, pk):
        reader = self.get_reader(pk)
        serializer = ReaderSerializer(instance=reader, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data="Reader Is Updated Successfully", status=200, content_type='application/json')
        else:
            return Response(data="Cant Update Reader", status=400, content_type='application/json')

    def delete(self, request, pk):
        reader = self.get_reader(pk)
        reader.delete()
        return Response(data="Reader Is Deleted Successfully", status=200, content_type='application/json')


class PublishersAPI(APIView):

    def get(self, request):
        publishers = Publisher.objects.all()
        if publishers:
            serializer = PublisherSerializer(journals, many=True)
            return Response(serializer.data, status=200, content_type='application/json')
        else:
            return Response(data="Cant Get Publishers Details", status=400, content_type='application/json')

    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        if not request.data:
            return Response(data="Error Message: Empty Body", status=400, content_type='application/json')
        elif Reader.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This Publisher Already Exists')

        if serializer.is_valid():
            serializer.save()
            return Response(data="New Publisher Added Successfully", status=201, content_type='application/json')
        return Response(data="Cant Add New Publisher", status=400, content_type='application/json')


class PublisherByIdAPI(APIView):

    def get_publisher(self, pk):
        try:
            return Publisher.objects.get(pk=pk)
        except Publisher.DoesNotExist:
            return Response(status=400)

    def get(self, request, pk):
        publisher = self.get_publisher(pk)
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)

    def put(self, request, pk):
        publisher = self.get_publisher(pk)
        serializer = PublisherSerializer(instance=publisher, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data="Publisher Is Updated Successfully", status=200, content_type='application/json')
        else:
            return Response(data="Cant Update Publisher", status=400, content_type='application/json')

    def delete(self, request, pk):
        publisher = self.get_publisher(pk)
        publisher.delete()
        return Response(data="Publisher Is Deleted Successfully", status=200, content_type='application/json')

