from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('<int:pk>', views.BlogPostView.as_view(), name='blog-post'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>',
         views.BloggerDetailView.as_view(),
         name='blogger-detail'),
]

urlpatterns += [
    path('create/', views.BlogPostCreate.as_view(), name='blog_create'),
    path('<int:pk>/update/',
         views.BlogPostUpdate.as_view(),
         name='blog_update'),
    path('<int:pk>/delete/',
         views.BlogPostDelete.as_view(),
         name='blog_delete'),
]