from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<tag>/', views.publicaciones, name='category'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
    path('create_post/', views.create_post, name='create_post'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
