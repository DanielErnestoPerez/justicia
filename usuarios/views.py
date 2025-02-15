from django.shortcuts import render, redirect, get_object_or_404
from justicia_app.models import Post
from .forms import ProfileForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count
from justicia_app .forms import CommentCreateForm, ReplyCreateForm
# Create your views here.

def profile(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except AttributeError:
            raise Http404()
    
    posts = profile.user.posts.all()

    if request.htmx:
        if 'top_posts' in request.GET:
            posts = profile.user.posts.annotate(
                num_likes=Count('likes')
            ).filter(num_likes__gt=0).order_by('-num_likes')
        
        elif 'top_comments' in request.GET:
            comments = profile.user.comments.annotate(
                num_likes=Count('likes')
            ).filter(num_likes__gt=0).order_by('-num_likes')
            
            comment_create_form = CommentCreateForm()
            reply_create_form = ReplyCreateForm()
            context2 = {
                'comments': comments,
                'comment_create_form': comment_create_form,
                'reply_create_form': reply_create_form
            }
            return render(request, 'snippets/loop_profile_comments.html', context2)
        
        elif 'liked_posts' in request.GET:
            posts = profile.user.liked_posts.order_by('-likedpost__created')
        
        return render(request, 'snippets/loop_profile_posts.html', {'posts': posts})

    context = {
        'posts': posts,
        'profile': profile,
    }
    return render(request, 'usuarios/profile.html', context)


@login_required
def profile_edit(request):
    profile_edit = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        profile_edit = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_edit.is_valid():
            profile_edit.save()
            return redirect('profile')
        
    if request.path == reverse('profile_onboarding'):
        template = 'usuarios/profile_onboarding.html'
    else:
        template = 'usuarios/profile_edit.html'
    return render(request, template, {'profile_edit': profile_edit})


@login_required
def profile_delete(request):
    user = request.user
    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, 'Profile deleted')
        return redirect('home')
    return render(request, 'usuarios/profile_delete.html')