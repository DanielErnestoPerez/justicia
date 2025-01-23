from django import forms
from .models import Post
class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo','imagen_fondo','imagen_portada', 'tags', 'resumen', 'contenido')
        labels = {
            'tags': 'Category',
        }
        widgets = {
            'resumen': forms.Textarea(attrs={
                'rows': 3,
                'cols': 45,
                'placeholder': 'Escribe un resumen aquí...',
                'class': 'custom_placeholder',
            }),
            'contenido': forms.Textarea(attrs={
                'rows': 5,
                'cols': 45,
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
