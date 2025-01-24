from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'real_name', 'email', 'location', 'bio')
        labels = {
            'real_name': 'Name',
        }
        widgets = {
            'image': forms.FileInput(),
            'bio': forms.Textarea(attrs={
                'rows': 3,
                'cols': 30,
                'placeholder': 'Write something about yourself...'
            })
        }