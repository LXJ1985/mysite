from django.contrib import admin
from .models import BlogType, Blog, ReadNum


# 使用装饰器注册模型
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'author', 'created_time', 'last_time')
    ordering = ('id',)


# 使用装饰器注册模型
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_type', 'author', 'read_num', 'created_time', 'last_time')
    ordering = ('id', )


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'blog')
    ordering = ('-read_num', )