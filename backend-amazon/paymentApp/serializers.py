from rest_framework import serializers
from .models import *

class contentsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Contents
        fields = '__all__'