#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Suger'
__date__ = '2018/7/21 下午6:19'

from django.urls import path

from .views import FavTopicView, UserFollowerView, UserFansView, UserCenterView, ModifyInfoView

app_name = 'users'
urlpatterns = [
    path('fav_topic/', FavTopicView.as_view(), name='fav_topic'),
    path('user_follower/', UserFollowerView.as_view(), name='user_follower'),
    path('user_fans/', UserFansView.as_view(), name='user_fans'),
    path('user_center/', UserCenterView.as_view(), name='user_center'),
    path('user_center_modify/', ModifyInfoView.as_view(), name='user_center_modify'),

]