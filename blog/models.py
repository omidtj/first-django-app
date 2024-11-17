from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    tags = TaggableManager()
    category =models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering =['-created_date']
        # verbose_name = 'پست'
        # verbose_name_plural = 'پست ها'
    def __str__(self):
        return f"{self.id} : {self.title}"
    
    @classmethod
    def get_all_published_posts(cls):
        return cls.objects.filter(status = 1).filter(published_date__lte = timezone.now())

    def counted_views_Inc(self):
        self.counted_views +=1
        self.save()
    def next_post(self,posts):
        # posts =Post.get_all_published_posts()
        return posts.filter(id__gt=self.id).order_by('id').first()
    def previous_post(self,posts):
        # posts =Post.get_all_published_posts()
        return posts.filter(id__lt=self.id).order_by('-id').first()
    # show blog in admin and sitemaps
    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved =models.BooleanField(default=False)




    
