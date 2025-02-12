from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Tag, Comment, Reply
from .forms import CreatePost, EditPost, CommentCreateForm, ReplyCreateForm
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
    create_post = CreatePost()
    if request.method == 'POST':
        create_post = CreatePost(request.POST, request.FILES)
        if create_post.is_valid():
            post = create_post.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('publicaciones')
    return render(request, 'justicia_app/create_post.html', {'create_post': create_post})

def read_post(request, post_id):
    post_to_read = get_object_or_404(Post, id=post_id)
    categories = Tag.objects.all()
    comment_create_form= CommentCreateForm()
    reply_create_form= ReplyCreateForm()
    context = {
        'post': post_to_read, 
        'categories': categories,
        'comment_create_form': comment_create_form,
        'reply_create_form': reply_create_form
        }
    return render(request, 'justicia_app/read_post.html', context )


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

@login_required
def comment_sent(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = post
            comment.save()
    return render(request, 'justicia_app/add_comment.html', {'comment': comment, 'post': post})

@login_required
def comment_delete(request, post_id):
    comment_to_delete = get_object_or_404(Comment, id=post_id, author=request.user)
    if request.method == 'POST':
        messages.success(request, 'Comment deleted successfully!')
        comment_to_delete.delete()
        return redirect('read_post', comment_to_delete.parent_post.id)
    return render(request, 'justicia_app/delete_comment.html', {'comment': comment_to_delete})

@login_required
def reply_sent(request, post_id):
    comment = get_object_or_404(Comment, id=post_id)
    if request.method == 'POST':
        form = ReplyCreateForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.parent_comment = comment
            reply.save()
    return redirect('read_post', comment.parent_post.id)


@login_required
def reply_delete(request, post_id):
    reply = get_object_or_404(Reply, id=post_id, author=request.user)
    if request.method == 'POST':
        messages.success(request, 'Reply deleted successfully!')
        reply.delete()
        return redirect('read_post', reply.parent_comment.parent_post.id)
    return render(request, 'justicia_app/delete_reply.html', {'reply': reply})

def like_toggle(model):
    def inner_func(func):
        def wrapper(request, *args, **kwargs):
            post = get_object_or_404(model, id=kwargs.get('post_id'))
            user_exist = post.likes.filter(username = request.user.username).exists()
            if post.author != request.user:
                if user_exist:
                    post.likes.remove(request.user)
                else:
                    post.likes.add(request.user)
            return func(request, post)
        return wrapper
    return inner_func

@login_required
@like_toggle(Post)
def like_post(request, post):
    return render(request, 'justicia_app/likes.html', {'post': post})


@login_required
@like_toggle(Comment)
def like_comment(request, post):
    return render(request, 'justicia_app/likes_comentarios.html', {'comment': post})

@login_required
@like_toggle(Reply)
def like_reply(request, post):
    return render(request, 'justicia_app/likes_replies.html', {'reply': post})