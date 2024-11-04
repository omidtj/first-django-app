from django.urls import path
from blog.views import *
app_name = 'blog'
urlpatterns = [
    # ("url address","view","name for html")
    path('', blog_view,name='index'),
    path('<int:pid>', blog_single,name='single')
]