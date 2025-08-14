from .models import Room, Topic
from django import forms


class RoomForm(forms.ModelForm):
    topic = forms.ModelChoiceField(
        queryset=Topic.objects.all(),
        empty_label="-Select a topic-"
    )

    class Meta:
        model = Room
        fields = ['name', 'topic', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter room name'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter room description'}),
        }
    