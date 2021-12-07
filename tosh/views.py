from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, JsonResponse
from django.db import IntegrityError
from django.urls import reverse
from .models import(User,
                    Information,
                    Experience,
                    Education,
                    Skillset,
                    Project,
                    Message)

# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')


def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if password != confirmation:
            return render(request, "registration/register.html", {"message":"Password must match"})
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'registration/register.html', {"message":"Username already exists"})

        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'registration/register.html')
