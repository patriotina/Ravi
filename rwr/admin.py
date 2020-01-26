from django.contrib import admin
from .models import Article, Comment, Photo
from django.utils.html import format_html
# Register your models here.


class Photo_list(admin.ModelAdmin):
    list_display = ['caption', 'pictumb']

    def pictumb(self, obj):
        return format_html('<img src="/static/{}" width=50px />'.format(obj.photo_file))


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Photo, Photo_list)