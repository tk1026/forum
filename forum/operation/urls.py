#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Suger'
__date__ = '2018/7/21 下午6:20'

from django.urls import path

from .views import CommentView, FavoriteView, RelationView

app_name = 'operation'
urlpatterns = [
    path('comment/<int:topic_id>', CommentView.as_view(), name='comment'),
    # 关注主题
    path('add_fav/', FavoriteView.as_view(), name='add_fav'),
    # 用户关系
    path('user_rel/', RelationView.as_view(), name='user_rel'),

]