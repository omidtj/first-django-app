from django import template
from blog.models import Post,Category,Comment

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts_count = Post.get_all_published_posts().count()
    return posts_count

@register.simple_tag(name='posts')
def function():
    posts = Post.get_all_published_posts()
    return posts

@register.simple_tag(name='totalcomments')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()

@register.filter
def snippet(value,arg=20):
    return value[:arg] + ' ...'

@register.inclusion_tag('blog/ctt-popular-posts.html')
def popularposts(arg=3):
    posts = Post.get_all_published_posts().order_by('-counted_views')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/ctt-post-categories.html')
def postcategories():
    posts = Post.get_all_published_posts().order_by('-published_date')
    categories = Category.objects.all()
    cat_dict ={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.inclusion_tag('blog/ctt-latest-posts.html')
def latestposts(arg=3):
    posts = Post.get_all_published_posts().order_by('-published_date')[:arg]
    return {'posts':posts}
    