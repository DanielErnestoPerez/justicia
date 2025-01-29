from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.CharField(max_length=300)
    contenido = models.TextField()
    imagen_fondo = models.ImageField(upload_to='posts')
    imagen_portada = models.ImageField(upload_to='posts')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField('Tag')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created']

class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    icons = models.FileField(upload_to='icons/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
