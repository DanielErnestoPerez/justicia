from django import forms
from .models import Post, Comment

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'tags','imagen_fondo','imagen_portada', 'resumen', 'contenido')
        labels = {
            'tags': 'Category',
        }
        widgets = {
            'titulo': forms.Textarea(attrs={
                'rows': 2,
                'cols': 45,
                'placeholder': 'Escribe un título aquí...',
                'class': 'custom_placeholder',
            }),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'custom_checkbox',
            }),
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
        }


class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'tags','imagen_fondo','imagen_portada', 'resumen', 'contenido')
        labels = {
            'tags': 'Category',
        }
        widgets = {
            'titulo': forms.Textarea(attrs={
                'rows': 2,
                'cols': 45,
                'placeholder': 'Escribe un título aquí...',
                'class': 'custom_placeholder',
            }),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'custom_checkbox',
            }),
            'resumen': forms.Textarea(attrs={
                'rows': 3,
                'cols': 85,
                'placeholder': 'Escribe un resumen aquí...',
                'class': 'custom_placeholder',
            }),
            'contenido': forms.Textarea(attrs={
                'rows': 10,
                'cols': 85,
                'placeholder': 'Escribe tu contenido aquí...',
                'class': 'custom_placeholder',
            }),
        }

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={
                'placeholder': 'Add a comment',
                'class': 'custom_comment_input',
                }),
        }
        labels = {
            'body': '',
        }
