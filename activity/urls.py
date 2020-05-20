from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import * 
from django.contrib.auth import views as auth_views

router = DefaultRouter()

urlpatterns = [
    path("", UserActivityView.as_view(), name='user-activity')
]