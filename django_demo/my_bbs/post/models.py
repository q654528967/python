from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class BaseModel(models.Model):
    class Meta:
        abstract = True
        ordering = ['-created_time']
    created_time = models.DateTimeField(auto_now_add=True, help_text=u'创建时间')
    last_modified = models.DateTimeField(auto_now=True, help_text=u'修改时间')

    def __str__(self):
        raise NotImplementedError


class Topic(BaseModel):
    class Meta:
        verbose_name = u'话题'
        verbose_name_plural = u'话题'
    title = models.CharField(max_length=255, unique=True, help_text='话题标题')
    content = models.TextField(help_text=u'话题内容')
    is_online = models.BooleanField(default=True, help_text=u'话题是否在线')
    user = models.ForeignKey(to=User, to_field='id', on_delete=models.CASCADE, help_text=u'关联用户表')

    def __str__(self):
        return f'{self.id}:{self.title[0:20]}'


class Comment(BaseModel):
    class Meta:
        verbose_name = u'话题评论'
        verbose_name_plural = u'话题评论'
    content = models.CharField(max_length=255, help_text='话题评论')
    topic = models.ForeignKey(to=Topic, to_field='id', on_delete=models.CASCADE, help_text=u'关联话题表')
    up = models.IntegerField(default=0, help_text=u'支持')
    down = models.IntegerField(default=0, help_text=u'反对')

    def __str__(self):
        return f'{self.id}:{self.content[0:20]}'

