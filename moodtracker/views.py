from django.shortcuts import render


def login_view(request):
    return render(request, 'login.html', {})


def registration_view(request):
    return render(request, 'registration.html', {})


def tracker_view(request):
    posts = [
        {'smile_ref': '/static/img/smiles/fear_smile_black.svg', 'mood': 'Страх', 'date': '14 апр 21:04',
         'image_ref': '/static/img/smiles/fear_photo.png'},

        {'smile_ref': '/static/img/smiles/fear_smile_black.svg', 'mood': 'Радость', 'date': '15 апр 19:33',
         'image_ref': '/static/img/default_image.png'},
    ]
    context = {'posts': posts}
    return render(request, 'tracker.html', context)


def friends_view(request):
    user_id = 78304
    friends = [
        {'image_ref': '/static/img/default_image.png', 'name': 'Котик', 'surname': 'Милашкин', 'login': 'cat322'},
        {'image_ref': '/static/img/default_image.png', 'name': 'Некотик', 'surname': 'Тожемилашкин',
         'login': 'notcat54'},
    ]
    add_friend_error = 'Не удалось найти пользователя с таким ID.'
    context = {'user_id': user_id, 'friends': friends, 'add_friend_error': add_friend_error }
    return render(request, 'friends.html', context)


def profile_view(request):
    user = {'image_ref': '/static/img/default_image.png', 'name': 'Булат', 'surname': 'Галсанов',
            'login': 'sadgirl1337'}
    context = {'user': user}
    return render(request, 'profile.html', context)


def post_publishing_view(request):
    return render(request, 'post_publishing.html', {})


def some_friend_view(request):
    return render(request, 'friend_page.html', {})
