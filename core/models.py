from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name
    

class Room(models.Model):
    name = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='rooms')
    description = models.TextField(blank=True)
    participants = models.ManyToManyField(User, related_name='rooms', blank=True)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:20]}"