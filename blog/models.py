from django.db import models
from django.urls import reverse  # used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from datetime import date, datetime
import uuid

# Create your models here.


class BlogPost(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200,
                             help_text="Enter title of blog post here.")
    post = models.TextField(help_text="Enter text of your blog post here.")

    # Foreign Key used because BlogPost can only have one Author, but authors can have multiple BlogPosts
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    post_date = models.DateField(auto_now_add=True)

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text='Unique ID for this post across whole site',
    )

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a page for this blog post.
        """
        return reverse('blog-post', args=[str(self.id)])


class Comment(models.Model):
    """
    Model representing a comment on a specific blog post.
    """
    name = models.TextField(max_length=500,
                            help_text="Enter your comment here.")
    post_date = models.DateTimeField(auto_now_add=True)

    # Foreign Key used because Comment can only have one Author, but authors can have multiple comments
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text='Unique ID for this comment across whole site',
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Blogger(models.Model):
    """
    Model representing a user that posts a blog post."
    """
    blogger = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text='Unique ID for this post across whole site',
    )

    bio = models.TextField(max_length=1000,
                           help_text='A brief biography of the user')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name