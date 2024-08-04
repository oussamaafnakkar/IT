from rest_framework import serializers
from .models import ITService

class ITServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITService
        fields = ['id', 'name', 'description', 'cost']
