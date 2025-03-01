from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'real_name', 'email')
    readonly_fields = ('created', 'updated')

admin.site.register(Profile, ProfileAdmin)