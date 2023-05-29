from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render

from blog.models import Category, Post

from .forms import RegisterForm


def home(request):
    featured_posts = Post.objects.filter(is_featured=True, status="Published")
    posts = Post.objects.filter(is_featured=False, status="Published")
    context = {
        "featured_posts": featured_posts,
        "posts": posts,
    }
    return render(request, "home.html", context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, "register.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect("home")
    form = AuthenticationForm()
    context = {"form": form}
    return render(request, "login.html", context)


def logout(request):
    auth.logout(request)
    return redirect("home")
