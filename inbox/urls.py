from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('search_users/', views.search_users, name='inbox_search_users'),
    path('inbox_notification/', views.inbox_notification, name='inbox_notification'),
    path('<conversation_id>/', views.inbox, name='inbox'),
    path('new_message/<recipient_id>/', views.new_message, name='inbox_new_message'),
    path('new_reply/<conversation_id>/', views.new_reply, name='inbox_new_reply'),
    path('notification/<conversation_id>/', views.notification, name='notification'),
]