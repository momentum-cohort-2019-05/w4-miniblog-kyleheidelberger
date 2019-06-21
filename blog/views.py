from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost, BlogComment, Blogger
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

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
    return render(
        request,
        'index.html',
    )


class BlogListView(generic.ListView):
    model = BlogPost
    paginate_by = 5


class BlogDetailView(generic.DetailView):
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
    fields = [
        'title',
        'post',
    ]


class BlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogs')


class BlogListbyAuthorView(generic.ListView):
    model = BlogPost
    paginate_by = 5
    template_name = 'blog/blog_list_by_author.html'

    def get_queryset(self):
        """
        Return list of Blog objects created by BlogAuthor (author id specified in URL)
        """
        id = self.kwargs['pk']
        target_author = get_object_or_404(BlogAuthor, pk=id)
        return Blog.objects.filter(author=target_author)

    def get_context_data(self, **kwargs):
        """
        Add BlogAuthor to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(BlogListbyAuthorView, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blogger'] = get_object_or_404(BlogAuthor,
                                               pk=self.kwargs['pk'])
        return context


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login. 
    """
    model = BlogComment
    fields = [
        'text',
    ]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['blogpost'] = get_object_or_404(BlogPost, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(BlogPost, pk=self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('blog-detail', kwargs={
            'pk': self.kwargs['pk'],
        })
