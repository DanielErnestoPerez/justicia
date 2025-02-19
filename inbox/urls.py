from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('conversation/<conversation_id>/', views.inbox, name='inbox'),
    path('search_users/', views.search_users, name='inbox_search_users'),
    path('new_message/<recipient_id>/', views.new_message, name='inbox_new_message'),
]