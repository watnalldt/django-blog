from django.shortcuts import redirect, render

from .models import Category, Post


def posts_by_category(request, category_id):
    # Fetch posts by category_id
    posts = Post.objects.filter(status="Published", category_id=category_id)
    # Use try/except when we want to do an action if the category doesn't exist
    try:
        category = Category.objects.get(id=category_id)
    except Exception:
        return redirect("home")
    # Use get_object_or_404 when we want to do an action if the category doesn't exist
    # category = Category.objects.get_object_or_404(id=category_id)
    context = {
        "posts": posts,
        "category": category,
    }
    return render(request, "posts_by_category.html", context)
