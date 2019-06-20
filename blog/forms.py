from django import forms
from models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost


class CommentForm(forms.ModelForm):
    class Meta:
        model = comment