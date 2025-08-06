from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Room, Post
from django.contrib.auth.decorators import login_required
from .forms import RoomForm

# Create your views here.

@login_required
def create_room(request):
    if request.method == 'PSOT':
        form  = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit = False)
            room.host = request.user
            room.participants.add(request.user)
            room.save()
            return redirect()
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



def room_detail(request, room_id):
    room = Room.objects.get(id = room_id)
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
            return redirect('room_detail', room_id = room.id)

    context = {
        'room':room,
        'posts': post
    }

    return render(request, 'core/room_detail.html', context)
