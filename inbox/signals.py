from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import InboxMessage
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage

@receiver(post_save, sender=InboxMessage)
def inbox_notification(sender, instance, created, **kwargs):
    message = instance
    site_domain = Site.objects.get(pk=1).domain
    if created:
        for participant in message.conversation.participants.all():
            if participant != message.sender and participant.emailaddress_set.filter(primary=True, verified=True).exists():
                try:
                    email_address = participant.emailaddress_set.get(primary=True, verified=True)
                    email_subject = f'New Message from {message.sender}'
                    email_body = f'You have received a new message from {site_domain}'
                    email = EmailMessage(
                        email_subject,
                        email_body,
                        from_email='noreply@' + site_domain,
                        to=[email_address.email],)
                    email.send()
                except:
                    pass