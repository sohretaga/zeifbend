from rest_framework import serializers
from .models import Chanel


class ChanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chanel
        fields = ['name', 'user_count', 'users', 'deposit', 'tour_count']