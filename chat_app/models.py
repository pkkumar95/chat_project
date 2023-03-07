from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username


class ChatRoom(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    members = models.ManyToManyField(User, related_name='rooms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('room-detail', args=[str(self.id)])

    
class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles', blank=True)

    def __str__(self):
        return self.user.username
