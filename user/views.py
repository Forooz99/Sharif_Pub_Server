from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser, Reader, Publisher
from .serializers import CustomUserSerializer, ReaderSerializer, PublisherSerializer
from rest_framework import serializers, status
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout


# GET: retrieve a resource
# PUT: insert & update stored resource
# POST: create new resource in collection
# DELETE: remove resource
def home(request):
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def signup(request):
    if request.data.get('role') == 'READER':
        print(request.data)
        reader = ReaderSerializer(data=request.data)
        if Reader.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This reader already exists')

        if reader.is_valid():
            reader.save()
            return Response(reader.data)
        else:
            print("Nooooo")
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.data.get('role') == 'PUBLISHER':
        publisher = PublisherSerializer(data=request.data)
        if Publisher.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This publisher already exists')

        if publisher.is_valid():
            publisher.save()
            return Response(publisher.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # validating for already existing data


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
    return Response(status=status.HTTP_200_OK)


def logout(request):
    logout(request)
    return redirect('home')


def delete_account(request):
    return redirect('home')


@api_view(['GET'])
def all_readers(request):
    pass


@api_view(['GET'])
def all_publishers(request):
    pass



