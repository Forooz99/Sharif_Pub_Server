from rest_framework import serializers
from .models import *


class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ['number', 'title', 'description', 'journal',
                  'releaseDate', 'category', 'img', 'file']


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['name', 'creationDate']
