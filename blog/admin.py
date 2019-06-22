from django.contrib import admin
from blog.models import BlogPost, BlogComment, Blogger

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(BlogComment)
admin.site.register(Blogger)

# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = (
#         'author',
#         'post_date',
#         'title',
#     )

# class BlogCommentAdmin(admin.ModelAdmin):
#     list_display = (
#         'author',
#         'post_date',
#     )

# class BloggerAdmin(admin.ModelAdmin):
#     list_display = (
#         'blogger',
#         'bio',
#     )


class BlogCommentsInline(admin.TabularInline):
    """
    Used to show 'existing' blog comments inline below associated blogs
    """
    model = BlogComment
    max_num = 0


class BlogPostAdmin(admin.ModelAdmin):
    """
    Administration object for Blog models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of blog comments in blog view (inlines)
    """
    list_display = ('title', 'author', 'post_date')
    inlines = [BlogCommentsInline]