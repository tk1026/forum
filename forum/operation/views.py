# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

from .forms import CommentForm
from .models import TopicComment, UserFavorite, UserRelation
from topics.models import Topic
from users.models import UserProfile


class CommentView(View):
    """
    发布评论
    """

    def post(self, request, topic_id):
        topic = Topic.objects.get(id=topic_id)
        login_user = UserProfile.objects.get(username=request.user.username)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            content = comment_form.cleaned_data['content']
            topic_comment = TopicComment()
            topic_comment.user = login_user
            topic_comment.topic = topic
            topic_comment.content = content
            topic_comment.save()
        return redirect(to='topic:detail', topic_id=topic_id)


class FavoriteView(View):
    """
    用户收藏
    """

    def post(self, request):
        fav_id = request.POST.get('fav_id', '')
        user = request.user
        exist_records = UserFavorite.objects.filter(user=user, fav_id=fav_id)
        if exist_records:
            exist_records.delete()
            return HttpResponse('{"status": "fail", "msg": "收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            user_fav.fav_id = fav_id
            user_fav.user = user
            user_fav.save()
            return HttpResponse('{"status": "success", "msg": "已收藏"}', content_type='application/json')


class RelationView(View):
    """
    用户关系
    """

    def post(self, request):
        # 发起关系用户id
        from_user_id = UserProfile.objects.get(username=request.user).id
        # 接受关系用户id
        to_user_id = request.POST.get('user_id', '')
        # 用户关系表
        user_rel = UserRelation()
        # 用户关系记录
        exist_rel = UserRelation.objects.filter(from_user=from_user_id, to_user=to_user_id)
        if exist_rel:
            exist_rel.delete()
            return HttpResponse('{"status": "fail", "msg": "关注"}', content_type='application/json')
        else:
            # 新增关注
            user_rel.from_user = from_user_id
            user_rel.to_user = to_user_id
            user_rel.rel_type = 2
            user_rel.save()
            # 反向关系
            exist_inverse_rel = UserRelation.objects.filter(from_user=to_user_id, to_user=from_user_id)
            if exist_inverse_rel.exists() and (int(exist_inverse_rel[0].rel_type) == (user_rel.rel_type)):
                return HttpResponse('{"status": "success", "msg": "互为关注"}', content_type='application/json')
            else:
                return HttpResponse('{"status": "success", "msg": "已关注"}', content_type='application/json')
