from app import models
from django import forms


class ImageForm(forms.ModelForm):

    image = forms.FileField(widget=forms.TextInput(
        attrs={
            "type": "file",
            "multiple": "True"
        }))

    class Meta:
        model = models.Image
        fields = ['image']
