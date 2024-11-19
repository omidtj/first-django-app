from django.contrib import admin
from blog.models import Post,Category,Comment
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display =('id',
                   'title',
                   'author',
                   'image',
                   'counted_views',
                   'status',
                   'login_require',
                   'published_date',
                   'created_date')
    list_filter = ('status','author')
    search_fields=['title','content']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): 
    pass  

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): 
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display =('name',
                   'post',
                   'approved',
                   'created_date',
                   'updated_date')
    list_filter = ('post','approved')
    search_fields=['name','post']


