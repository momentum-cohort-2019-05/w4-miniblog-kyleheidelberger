from django.shortcuts import render
from blog.models import BlogPost, Comment, Blogger
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    """
    View function for home page of site.
    """

    # Generate counts of some of the main objects
    num_blog_posts = BlogPost.objects.all().count()

    context = {
        'num_blog_posts': num_blog_posts,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BlogListView(generic.ListView):
    model = BlogPost
    paginate_by = 5


class BlogPostView(generic.DetailView):
    model = BlogPost


class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 5


class BloggerDetailView(generic.DetailView):
    model = Blogger

class BlogPostCreate(CreateView):
    model = BlogPost
    fields = '__all__'

class BlogPostUpdate(UpdateView):
    model = BlogPost
    fields = ['title', 'post',]

class BlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogs')