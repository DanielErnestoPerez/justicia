from django import forms
from .models import Post
class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'contenido','imagen', 'tags')
        labels = {
            'tags': 'Category',
        }
        widgets = {
            'contenido': forms.Textarea(attrs={
                'rows': 5,
                'cols': 24,
                'placeholder': 'Escribe tu contenido aquí...',
                'class': 'custom_placeholder',
            }),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'custom_checkbox',
            }),
        }


class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('contenido', 'tags')
        labels = {
            'tags': 'Category',
        }
        widgets = {
            'contenido': forms.Textarea(attrs={
                'rows': 3,
                'cols': 30,
                'placeholder': 'Escribe tu contenido aquí...',
                'class': 'custom_placeholder',
            }),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'custom_checkbox',
            }),
        }
