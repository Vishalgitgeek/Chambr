from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Room, Post, Profile
from django.contrib.auth.decorators import login_required
from .forms import RoomForm, ProfileForm
from django.conf import settings
from django.contrib.auth import get_user_model

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
            return redirect('room_detail', room_name=room.name)
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
    posts = room.posts.all().order_by('-created_at')
    participants = room.participants.all()

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
        'posts': posts,
        'participants': participants
    }

    return render(request, 'core/room_detail.html', context)


def profile_view(request, username):
    User = get_user_model() 
    user_profile = get_object_or_404(User, username = username)

    # get or create profile if not exts
    profile, created = Profile.objects.get_or_create(user=user_profile)
    context = {
        'user_profile': user_profile,
        'profile': profile
    }
    return render(request, 'core/user_profile.html',context)


@login_required
def edit_profile(request):
    # get or crete profile if not exis
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile',  username = request.user.username)

    else:
        form = ProfileForm(instance = profile)

    return render(request, 'core/edit_user_profile.html', {'form':form})