# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2018/5/11 12:48
# @Author: Administrator
# @File: views.py

from django.shortcuts import render_to_response
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import get_seven_days_read_data
from blog.models import BlogType, Blog


def home(request):
    context_type = ContentType.objects.get_for_model(Blog)
    read_nums = get_seven_days_read_data(context_type)

    context = {'read_nums': read_nums,
               }
    return render_to_response('home.html', context)


def about(request):
    # 获取日期归档统计数量:
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year, created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    # 获取博客分类统计数量 方法一： annotate()
    context = {'blog_types': BlogType.objects.annotate(blog_count=Count('blog')),
               'blog_dates': blog_dates_dict}
    return render_to_response('about.html', context)



