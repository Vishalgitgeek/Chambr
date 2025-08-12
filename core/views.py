from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Room, Post
from django.contrib.auth.decorators import login_required
from .forms import RoomForm

# Create your views here.

@login_required
def create_room(request):
    if request.method == 'POST':
        form  = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit = False)
            room.host = request.user
            room.save()
            room.participants.add(request.user)
            return redirect('room_detail', room_id=room.id)
    else:
        form = RoomForm()

    return render(request, 'core/create_room.html', {'form':form})



def home(request):
    topic = Topic.objects.all()
    room = Room.objects.all()

    context = {
        'tpics': topic,
        'rooms': room
    }

    return render(request, 'core/home.html', context)


@login_required(login_url='login')
def room_detail(request,  room_name):
    room = Room.objects.get(name = room_name)
    post = Post.objects.all().order_by('-created_at')

    if request.user.is_authenticated and request.method == 'POST':
        content = request.POST.get('content')
        image = request.FILES.get('image')

        if content or image:
            Post.objects.create(
                user = request.user,
                room = room,
                content = content,
                image = image
            )
            room.participants.add(request.user)
            return redirect('room_detail', room_name = room.name)

    context = {
        'room':room,
        'posts': post
    }

    return render(request, 'core/room_detail.html', context)
