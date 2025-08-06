from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Room, Post
# from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    topic = Topic.objects.all()
    room = Room.objects.all()

    context = {
        'tpics': topic,
        'rooms': room
    }

    return render(request, 'core/home.html', context)



def room_detail(request, room_id):
    room = Room.objects.get(id = room_id)
    post = Post.objects.all().order_by('-created_at')

    context = {
        'room':room,
        'posts': post
    }

    return render(request, 'core/room_detail.html', context)
