from django import forms
from .models import InboxMessage

class InboxNewMessageForm(forms.ModelForm):
    class Meta:
        model = InboxMessage
        fields = ['body']
        labels = {
            'body': '',
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Write your message',
                'rows': 3,
                'class': 'custom_inbox_textarea',
                }
                )},