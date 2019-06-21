from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('blogs/', views.BlogListView.as_view(), name='blogs'),
#     path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
#     path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
#     path('blogger/<int:pk>',
#          views.BloggerDetailView.as_view(),
#          name='blogs-by-author'),
#     path('blog/<int:pk>/comment/',
#          views.BlogCommentCreate.as_view(),
#          name='blog_comment'),
# ]

# urlpatterns += [
#     path('create/', views.BlogPostCreate.as_view(), name='blog_create'),
#     path('<int:pk>/update/',
#          views.BlogPostUpdate.as_view(),
#          name='blog_update'),
#     path('<int:pk>/delete/',
#          views.BlogPostDelete.as_view(),
#          name='blog_delete'),
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogger/<int:pk>', views.BloggerListView.as_view(), name='blogs-by-author'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blog/<int:pk>/comment/', views.BlogCommentCreate.as_view(), name='blog_comment'),
]