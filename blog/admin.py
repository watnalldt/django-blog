from django.contrib import admin

from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "created_at", "updated_at")


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "title",
        "category",
        "author",
        "is_featured",
        "status",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "title",
        "category__category_name",
        "status",
    )
    list_editable = ("is_featured", "status")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
