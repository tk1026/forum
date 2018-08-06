#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Suger'
__date__ = '2018/7/21 下午6:09'

from django.urls import path

from .views import IndexView, PubTopicView, CommitTopicView, DetailView, MemberView

app_name = 'topic'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # 主题详情
    path('detail/<int:topic_id>/', DetailView.as_view(), name='detail'),
    # 发布主题
    path('pub/<str:username>/', PubTopicView.as_view(), name='pub'),
    # 提交主题
    path('pub/<str:username>/commit', CommitTopicView.as_view(), name='pub_commit'),
    # 注册会员
    path('member/<str:username>/', MemberView.as_view(), name='member'),

]