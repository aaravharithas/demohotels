from rest_framework import serializers
from .models import Todo, Hotel

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'