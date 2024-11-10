from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts_count = Post.get_all_published_posts().count()
    return posts_count

@register.simple_tag(name='posts')
def function():
    posts = Post.get_all_published_posts()
    return posts

@register.filter
def snippet(value,arg=20):
    return value[:arg] + ' ...'

@register.inclusion_tag('popularposts.html')
def popularposts():
    posts = Post.get_all_published_posts().order_by('-published_date')[:3]
    return {'posts':posts}
    