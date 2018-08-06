# -*- coding:utf-8 -*-

from django.db import models

from users.models import UserProfile
from topics.models import Topic


class TopicComment(models.Model):
    """
    用户对主题评论
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name=u"主题")
    content = models.TextField(verbose_name=u"评论内容")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户主题评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据ID")
    add_time = models.DateTimeField(auto_now=True, verbose_name=u"收藏时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserRelation(models.Model):
    """
    用户关系
    """
    from_user = models.IntegerField(null=True, blank=True, verbose_name=u"关系发起者")
    to_user = models.IntegerField(null=True, blank=True, verbose_name=u"关系接受者")
    rel_type = models.CharField(choices=((1, "粉丝"), (2, "关注"), (3, "互相关注")), max_length=1, verbose_name="关系类型")

    class Meta:
        verbose_name = u"用户关系"
        verbose_name_plural = verbose_name
