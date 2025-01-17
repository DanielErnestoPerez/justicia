from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='posts', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField('Tag')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

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
