from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ChatRoom, Message, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'description', 'created_by', 'created_at']
        read_only_fields = ['created_by', 'created_at']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'text', 'chat_room', 'user', 'created_at']
        read_only_fields = ['user', 'created_at']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio', 'profile_picture']
        read_only_fields = ['user']
