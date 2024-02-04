from rest_framework import serializers
from .models import Reader, Publisher


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'

        error_messages = {
            'email': {
                'required': 'Email Required',
                'blank': 'No Blank Email',
            },
            'password': {
                'required': 'Password Required',
                'blank': 'No Blank Password',
            },
            'type': {
                'required': 'READER Type Required',
                'blank': 'No Blank READER',
            },
        }


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

    error_messages = {
        'email': {
            'required': 'Email Required',
            'blank': 'No Blank Email',
        },
        'password': {
            'required': 'Password Required',
            'blank': 'No Blank Password',
        },
        'type': {
            'required': 'READER Type Required',
            'blank': 'No Blank READER',
        },
        'owned_journal': {
            'required': "Publisher's Journal Name Required",
            'blank': "No Blank Publisher's Journal Name",
        },
    }
