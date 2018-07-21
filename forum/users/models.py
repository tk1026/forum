# -*- coding:utf-8 -*-

from django.db import models


class UserProfile(models.Model):
    """
    用户信息
    """
    username = models.CharField(max_length=100, verbose_name=u"用户名")
    nick_name = models.CharField(max_length=20, verbose_name=u"昵称", default="")
    password = models.CharField(max_length=128, verbose_name=u"密码")
    email = models.CharField(max_length=254, verbose_name=u"邮箱")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"电话")
    avatar = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100,
                               verbose_name=u"头像")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=u"加入时间")
    last_login = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=u"最后登录")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserFollower(models.Model):
    """
    用户粉丝
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, verbose_name=u"用户")
    follower_name = models.CharField(max_length=100, verbose_name=u"粉丝名称")

    class Meta:
        verbose_name = u"用户粉丝"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.follower_name
