from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):

    empty_value_display = '-empty-'
    list_display = ('title','author','status','published_date','created_date')
    list_filter = ('status','author')
    search_fields = ['author','title','content']

class CommentAdmin(admin.ModelAdmin):
    
    empty_value_display = '-empty-'
    list_display = ('post','approved','created_date')
    list_filter = ('post','approved')
    search_fields = ['post','email']

admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)