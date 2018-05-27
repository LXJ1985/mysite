from django.contrib import admin
from .models import BlogType, Blog


# 使用装饰器注册模型
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'author', 'created_time', 'last_time')
    ordering = ('id',)


# 使用装饰器注册模型
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog_type', 'get_blog_read_num', 'author', 'created_time', 'last_time')
    ordering = ('id', )

