from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Tag
from .forms import CreatePost, EditPost
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

def redes_sociales(request):
    return render(request, 'justicia_app/redes_sociales.html')


@login_required
def create_post(request):
    if request.method == 'POST':
        create_post = CreatePost(request.POST, request.FILES)
        if create_post.is_valid():
            messages.success(request, 'Post created successfully!')
            create_post.save()
            return redirect('publicaciones')
    else:
        create_post = CreatePost()
    return render(request, 'justicia_app/create_post.html', {'create_post': create_post})

def read_post(request, post_id):
    post_to_read = get_object_or_404(Post, id=post_id)
    categories = Tag.objects.all()
    return render(request, 'justicia_app/read_post.html', {'post': post_to_read, 'categories': categories})


@login_required
def edit_post(request, post_id):
    post_to_edit = get_object_or_404(Post, id=post_id, author=request.user)
    edit_post = EditPost(instance=post_to_edit)
    if request.method == 'POST':
        edit_post = EditPost(request.POST, instance=post_to_edit)
        if edit_post.is_valid():
            messages.success(request, 'Post updated successfully!')
            edit_post.save()
            return redirect('publicaciones')
        else:
            print('Error updating', edit_post.errors)
    return render(request, 'justicia_app/edit_post.html', {'post': post_to_edit, 'edit_post': edit_post})

@login_required
def delete_post(request, post_id):
    post_to_delete = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        messages.success(request, 'Post deleted successfully!')
        post_to_delete.delete()
        return redirect('publicaciones')
    return render(request, 'justicia_app/delete_post.html', {'post': post_to_delete})