from django.db import models
from django.contrib.auth.models import User
import uuid
from cloudinary.models import CloudinaryField
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.CharField(max_length=300)
    contenido = models.TextField()
    imagen_fondo = CloudinaryField('image',folder= 'backgrounds', null=True)
    imagen_portada = CloudinaryField('image', folder= 'portadas', null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    likes = models.ManyToManyField(User, related_name="liked_posts", through='LikedPost')
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


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField()
    likes = models.ManyToManyField(User, related_name='liked_comments', through='LikedComment')
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")
        ordering = ['-created']

    def __str__(self):
        try:
            return f'{self.author.username}:{self.body[:30]}'
        except AttributeError:
            return f'no author :{self.body[:30]}'

class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='replies')
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    body = models.CharField()
    likes = models.ManyToManyField(User, related_name='liked_reply', through='LikedReply')
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        verbose_name = ("Reply")
        verbose_name_plural = ("Replies")
        ordering = ['-created']

    def __str__(self):
        try:
            return f'{self.author.username}:{self.body[:30]}'
        except AttributeError:
            return f'no author :{self.body[:30]}'

class LikedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} : {self.post.titulo}'
    
    class Meta:
        verbose_name = 'LikedPost'
        verbose_name_plural = 'LikedPosts'


class LikedComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} : {self.comment.body[:30]}'
    
    class Meta:
        verbose_name = 'LikedComment'
        verbose_name_plural = 'LikedComments'


class LikedReply(models.Model):
    comment = models.ForeignKey(Reply, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} : {self.reply.body[:30]}'
    
    class Meta:
        verbose_name = 'LikedReply'
        verbose_name_plural = 'LikedReplies'