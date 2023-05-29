from django.contrib import admin

from .models import About, SocialLink


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        return count == 0


admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)
