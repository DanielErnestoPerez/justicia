from django.contrib import admin
from .models import Post, Tag, Comment, Reply, LikedPost, LikedComment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'resumen', 'imagen_fondo')
    readonly_fields = ('created', 'updated')

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(LikedPost)
admin.site.register(LikedComment)
