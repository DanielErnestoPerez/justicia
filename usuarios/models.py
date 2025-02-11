from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image',folder= 'profile_photo', null=True)
    real_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return str(self.user)
    
    @property
    def avatar(self):
        try:
            avatar = self.image.url
        except AttributeError:
            avatar = static('img/default_user.png')
        return avatar
    
    @property
    def name(self):
        if self.real_name:
            name = self.real_name
        else:
            name = self.user.username
        return name