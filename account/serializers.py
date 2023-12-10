from rest_framework import serializers
from .models import CustomUser
from django.core.files import File
from django.conf import settings

import os
import random

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password',
                  'first_name', 'last_name', 'balacne', 'level',
                  'leaderboard', 'total_game_count', 'won_game_count']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])

        avatars_path = os.path.join(settings.STATIC_ROOT, 'avatars')
        if os.path.exists(avatars_path):
            avatars = [f for f in os.listdir(avatars_path) if os.path.isfile(os.path.join(avatars_path, f))]
            if avatars:
                avatar_file_name = random.choice(avatars)
                avatar_file_path = os.path.join(avatars_path, avatar_file_name)
                with open(avatar_file_path, 'rb') as avatar_file:
                    user.avatar.save(avatar_file_name, File(avatar_file), save=False)
        user.save()

        return user

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'won_game_count']