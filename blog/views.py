from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .models import Category, Comment, Post


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


def posts(request, slug):
    single_post = get_object_or_404(Post, slug=slug, status="Published")
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_post
        comment.comment = request.POST.get["comment"]
        comment.save()
        return HttpResponseRedirect(request.path_info)

    # Comments
    comments = Comment.objects.filter(post=single_post)
    comment_count = comments.count()
    context = {
        "single_post": single_post,
        "comments": comments,
        "comment_count": comment_count,
    }
    return render(request, "posts.html", context)


def search(request):
    keyword = request.GET.get("keyword")
    terms = Post.objects.filter(
        Q(title__icontains=keyword)
        | Q(short_description__icontains=keyword)
        | Q(blog_body__icontains=keyword),
        status="Published",
    )
    context = {
        "terms": terms,
        "keyword": keyword,
    }
    return render(request, "search.html", context)
