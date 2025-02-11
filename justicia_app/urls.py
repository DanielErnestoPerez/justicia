from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<tag>/', views.publicaciones, name='category'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
    path('redes_sociales/', views.redes_sociales, name='redes_sociales'),
    path('create_post/', views.create_post, name='create_post'),
    path('read_post/<post_id>/', views.read_post, name='read_post'),
    path('edit_post/<post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<post_id>/', views.delete_post, name='delete_post'),
    path('comment_sent/<post_id>/', views.comment_sent, name='comment_sent'),
    path('comment_delete/<post_id>/', views.comment_delete, name='comment_delete'),
    path('reply_sent/<post_id>/', views.reply_sent, name='reply_sent'),
    path('reply_delete/<post_id>/', views.reply_delete, name='reply_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
