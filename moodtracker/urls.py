"""
URL configuration for moodtracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from moodtracker.views import (
    login_view,
    registration_view,
    tracker_view,
    friends_view,
    profile_view,
    post_publishing_view,
    some_friend_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view),  # /login
    path('registration/', registration_view),
    path('registration/', registration_view),
    path('tracker/', tracker_view),
    path('friends/', friends_view),
    path('profile/', profile_view),

    path('tracker/post_publishing/', post_publishing_view),
    path('friends/some_friend/', some_friend_view),

]
