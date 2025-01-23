from django.shortcuts import render, redirect
from .models import Post, Tag
from .forms import CreatePost, EditPost
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'justicia_app/home.html')

def publicaciones(request, tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag = Tag.objects.get(slug=tag)
    else:
        posts = Post.objects.all()

    categories = Tag.objects.all()
    return render(request, 'justicia_app/publicaciones.html', 
                {'posts': posts, 'categories': categories, 'tag': tag})


def create_post(request):
    if request.method == 'POST':
        create_post = CreatePost(request.POST, request.FILES)
        if create_post.is_valid():
            messages.success(request, 'Post created successfully!')
            create_post.save()
            return redirect('home')
    else:
        create_post = CreatePost()
    return render(request, 'justicia_app/create_post.html', {'create_post': create_post})