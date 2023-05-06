from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from fer import FER
from PIL import Image
import cv2


def login_view(request):
    if request.method == 'POST':
        user_login = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(login=user_login, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('tracker'))
        else:
            message = 'Неверно введен логин или пароль.'
    return render(request, 'login.html', locals())


def registration_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('tracker'))
        else:
            message = 'Проверьте правильность введенных полей.'
    return render(request, 'registration.html', locals())


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required(login_url='login')
def tracker_view(request):
    form = TrackerForm(instance=request.user)
    trackers = Tracker.objects.filter(user=request.user)
    if request.method == 'POST':
        form = TrackerForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            tracker = Tracker.objects.create(image=image, user=request.user)
            emotion_locale = {'angry': "Злость", 'disgust': "Отвращение", 'fear': "Страх", 'happy': "Счастье",
                              'neutral': "Нейтральный", 'sad': "Грусть", 'surprise': "Удивление"}
            img = cv2.imread(tracker.image.path)
            detector = FER()
            detector.detect_emotions(img)
            emotion, score = detector.top_emotion(img)
            if emotion:
                tracker.mood = emotion_locale[emotion]
                tracker.save()
                return HttpResponseRedirect(reverse('post_publishing', kwargs={'id': tracker.id}))
            else:
                tracker.delete()
                message = 'Не удалось распознать лицо'
    return render(request, 'tracker.html', locals())


@login_required(login_url='login')
def post_publishing_view(request, id):
    try:
        tracker = Tracker.objects.get(id=id)
        return render(request, 'post_publishing.html', locals())
    except Tracker.DoesNotExist:
        return HttpResponseRedirect(reverse('tracker'))


def delete_tracker_view(request, id):
    try:
        tracker = Tracker.objects.get(id=id)
        tracker.delete()
    except Tracker.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('tracker'))


@login_required(login_url='login')
def friends_view(request):
    add_friend_error = 'Не удалось найти пользователя с таким ID.'
    friends = Friend.objects.filter(user=request.user)
    return render(request, 'friends.html', locals())


@require_http_methods(["POST"])
@login_required(login_url='login')
def search_friend_view(request):
    try:
        unique_id = request.POST.get('unique_id')
        friend = User.objects.get(unique_id=unique_id)
        if Friend.objects.filter(user=request.user, friend=friend):
            message = 'Пользователь уже является вашим другом.'
        elif request.user.unique_id == unique_id:
            message = 'Это ваш ID. Введите ID другого пользователя.'
        else:
            Friend.objects.create(user=request.user, friend=friend)
    except User.DoesNotExist:
        message = 'Не удалось найти пользователя с таким ID.'
    friends = Friend.objects.filter(user=request.user)
    return render(
        request,
        'friends_list.html',
        locals(),
        True
    )


@login_required(login_url='login')
def delete_with_friend_view(request, id):
    try:
        Friend.objects.get(friend_id=id).delete()
        return HttpResponseRedirect(reverse('friends'))
    except Friend.DoesNotExist:
        return HttpResponseRedirect(reverse('friend'))


@login_required(login_url='login')
def some_friend_view(request, id):
    friend = User.objects.get(id=id)
    trackers = Tracker.objects.filter(user=friend)
    return render(request, 'friend_page.html', locals())


@login_required(login_url='login')
def profile_view(request):
    form = ProfileForm(instance=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    return render(request, 'profile.html', locals())
