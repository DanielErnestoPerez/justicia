from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('profile_onboarding/', views.profile_edit, name='profile_onboarding'),
    path('profile_delete/', views.profile_delete, name='profile_delete'),
    path('<username>/', views.profile, name='user_profile'),
]
