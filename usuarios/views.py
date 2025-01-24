from django.shortcuts import render, redirect, get_object_or_404
from justicia_app.models import Post
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.http import Http404
# Create your views here.

def profile(request, username=None):
    posts = Post.objects.all()
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404()
    return render(request, 'usuarios/profile.html', {'posts': posts, 'profile': profile})

def profile_edit(request):
    profile_edit = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        profile_edit = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_edit.is_valid():
            profile_edit.save()
            return redirect('profile')
    return render(request, 'usuarios/profile_edit.html', {'profile_edit': profile_edit})


def profile_delete(request):
    return render(request, 'usuarios/profile_delete.html')