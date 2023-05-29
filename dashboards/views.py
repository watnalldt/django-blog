from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import slugify

from blog.models import Category, Post

from .forms import AddUserForm, CategoryForm, EditUserForm, PostForm


@login_required(login_url="login")
def dashboard(request):
    category_count = Category.objects.all().count()
    posts_count = Post.objects.all().count()
    context = {
        "category_count": category_count,
        "posts_count": posts_count,
    }
    return render(request, "dashboards/dashboard.html", context)


def categories(request):
    return render(request, "dashboards/categories.html")


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    form = CategoryForm()
    context = {
        "form": form,
    }
    return render(request, "dashboards/add_category.html", context)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("categories")
    form = CategoryForm(instance=category)
    context = {
        "form": form,
        "category": category,
    }
    return render(request, "dashboards/edit_category.html", context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("categories")


def posts(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "dashboards/posts.html", context)


def add_post(request):  # sourcery skip: extract-method
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # tempporarily savibg the form
            post.author = request.user
            post.save()
            title = form.cleaned_data["title"]
            post.slug = f"{slugify(title)-str(post.id)}"
            post.save()
            return redirect("posts")

    form = PostForm()
    context = {
        "form": form,
    }

    return render(request, "dashboards/add_post.html", context)


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.title = form.cleaned_data["title"]
            post.slug = f"{slugify(post.title)}-{str(post.id)}"
            post.save()
            return redirect("posts")
    form = PostForm(instance=post)
    context = {
        "form": form,
        "post": post,
    }

    return render(request, "dashboards/edit_post.html", context)


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("posts")


def users(request):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, "dashboards/users.html", context)


def add_user(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("users")
    form = AddUserForm()
    context = {"form": form}
    return render(request, "dashboards/add_user.html", context)


def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("users")

    form = EditUserForm(instance=user)
    context = {"form": form, "user": user}
    return render(request, "dashboards/edit_user.html", context)


def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect("users")
