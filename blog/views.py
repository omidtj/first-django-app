from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from blog.models import Post
# آدرس شروع از فولدر تمپلیتس
def blog_view(request):
    posts = Post.objects.filter(status = 1).filter(published_date__lte = timezone.now())
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    posts = Post.objects.filter(status = 1)
    post = get_object_or_404(posts,pk=pid)
    post.counted_views_Inc()
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)



  
