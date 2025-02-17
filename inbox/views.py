from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import InboxMessage, Conversation
# Create your views here.

@login_required
def inbox(request):
    conversation = Conversation.objects.first()
    context = {
        'conversation': conversation,
    }
    return render(request, 'inbox/inbox.html', context)
