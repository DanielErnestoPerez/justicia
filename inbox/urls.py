from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('conversation/<conversation_id>/', views.inbox, name='inbox'),
    path('search_users/', views.search_users, name='inbox_search_users'),
]