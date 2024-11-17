from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
# آدرس شروع از فولدر تمپلیتس
def blog_view(request,**kwargs):
    posts = Post.get_all_published_posts()
    if kwargs.get('cat_name') != None :
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None :
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None :
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    paginator = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(1)    
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    published_posts = Post.get_all_published_posts()
    post = get_object_or_404(published_posts,pk=pid)
    comments=Comment.objects.filter(post=post.id,approved=True)
    next_post = post.next_post(published_posts)
    previous_post = post.previous_post(published_posts)
    post.counted_views_Inc()
    context = {
                'post':post ,
                'next_post':next_post ,
                'previous_post':previous_post,
                'comments':comments}
    return render(request,'blog/blog-single.html',context)

def blog_search(request):
    posts = Post.get_all_published_posts()
    if request.method == 'GET':
        # walrus
        if s := request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)


  
