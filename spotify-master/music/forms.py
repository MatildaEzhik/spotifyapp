from django import forms

from music.models import Music


class AddMusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = 'name', 'image', 'file', 'album', 'genres'
