from django.urls import path
from blog.views import *
app_name = 'blog'
urlpatterns = [
    # ("url address","view","name for html")
    path('', blog_view,name='index'),
    path('category/<str:cat_name>', blog_view,name='category'),
    path('author/<str:author_username>', blog_view,name='author'),
    path('tag/<str:tag_name>', blog_view,name='tag'),
    path('search/',blog_search,name='search'),
    path('<int:pid>', blog_single,name='single'),
]