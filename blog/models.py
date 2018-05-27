from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create BlogType and Blog models below.
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(max_length=30)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    # content = models.TextField()
    content = RichTextField()   # 富文本
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)

    def read_num(self):
        # 返回BLOG阅读数量
        return self.readnum.read_num

    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-created_time']


class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING)

