from .models import Room, Post
from django import forms

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'topic', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }