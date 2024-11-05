from django.contrib import admin
from blog.models import Post,Category
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
                   'published_date',
                   'created_date')
    list_filter = ('status','author')
    search_fields=['title','content']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): 
    pass  
