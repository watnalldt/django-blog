from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Category, Post


def home(request):
    featured_posts = Post.objects.filter(is_featured=True, status="Published")
    posts = Post.objects.filter(is_featured=False, status="Published")
    context = {
        "featured_posts": featured_posts,
        "posts": posts,
    }
    return render(request, "home.html", context)
