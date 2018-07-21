# -*- coding:utf-8 -*-

from django.db import models

from users.models import UserProfile


class TopicTag(models.Model):
    """
    主题标签
    """
    name = models.CharField(max_length=100, verbose_name=u"标签名")

    class Meta:
        verbose_name = u"主题标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Topic(models.Model):
    """
    主题
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    title = models.CharField(max_length=100, verbose_name=u"标题")
    content = models.TextField(verbose_name=u"主题内容")
    tags = models.ManyToManyField(TopicTag, null=True, blank=True)
    read_nums = models.IntegerField(default=0, verbose_name=u"阅读次数")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"主题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
