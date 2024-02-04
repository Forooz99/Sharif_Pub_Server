from rest_framework import serializers
from .models import Journal, Volume


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

    error_messages = {
        'name': {
            'required': "Journal's Name Required",
            'blank': "No Blank Journal's Name",
        }
    }


class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = '__all__'

    error_messages = {
        'number': {
            'required': "Volume's Number Required",
            'blank': "No Blank Volume's Number",
        },
        'title': {
            'required': "Volume's Title Required",
            'blank': "No Blank Volume's Title",
        },
        'journal': {
            'required': "Volume's Journal Required",
            'blank': "No Blank Volume's Journal",
        },
    }
