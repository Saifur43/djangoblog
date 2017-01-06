from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html', {'content': ['If You Are Interested Email me at', 'saifurrahmany43@mail.com']})
