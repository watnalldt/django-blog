from django.conf import settings
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published", "Published"),
)


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
