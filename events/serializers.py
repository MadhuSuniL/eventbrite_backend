from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event

class EventSerialzer(serializers.ModelSerializer):
    likes = serializers.IntegerField(read_only=True)
    class Meta:
        model = Event
        fields = '__all__'
        