from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from moodtracker import settings
from moodtracker.views import (
    login_view,
    logout_view,
    registration_view,
    tracker_view,
    friends_view,
    search_friend_view,
    delete_with_friend_view,
    profile_view,
    post_publishing_view,
    some_friend_view,
    delete_tracker_view
)

urlpatterns = [
    path('login/', login_view, name="login"),  # /login
    path('logout/', logout_view, name="logout"),  # /login
    path('registration/', registration_view, name='registration'),

    path('', tracker_view, name='tracker'),

    path('friends/', friends_view, name='friends'),
    path('search_friend/', search_friend_view, name='search_friend'),
    path('some_friend/<int:id>', some_friend_view, name='friend'),
    path('delete_friend/<int:id>', delete_with_friend_view, name='delete_friend'),

    path('profile/', profile_view, name='profile'),

    path('post_publishing/<int:id>', post_publishing_view, name="post_publishing"),
    path('delete_tracker/<int:id>', delete_tracker_view, name="delete_tracker"),

    path('friends/some_friend/', some_friend_view),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
