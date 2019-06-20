from django.contrib import admin
from blog.models import BlogPost, Comment

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Comment)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'post_date',
        'title',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'post_date',
    )
