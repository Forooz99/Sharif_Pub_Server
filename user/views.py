from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Reader, Publisher
from .serializers import UserSerializer
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
def add_user(request):
    user = UserSerializer(data=request.data)

    # validating for already existing data
    if User.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This user already exists')

    if user.is_valid():
        user.save()
        return Response(user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_users(request):
    # checking for the parameters from the URL
    if request.query_params:
        users = User.objects.filter(**request.query_params.dict())
    else:
        users = User.objects.all()

    # if there is something in items else raise error
    if users:
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_user(request, pk):
    user = User.objects.get(pk=pk)
    data = UserSerializer(instance=user, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
