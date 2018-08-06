# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .forms import PubTopicForm
from .models import Topic
from users.models import UserProfile
from operation.forms import CommentForm
from operation.models import UserRelation
from forum.settings import MEDIA_URL


class IndexView(View):
    """
    主题列表展示
    """
    template_index = 'index.html'

    def get(self, request):
        topic_list = Topic.objects.all().order_by('-add_time')
        paginator = Paginator(topic_list, 5)
        page = request.GET.get('page')
        try:
            topics = paginator.page(page)
        except PageNotAnInteger:
            topics = paginator.page(1)
        except EmptyPage:
            topics = paginator.page(paginator.num_pages)
        # 关注/粉丝
        follower = UserRelation.objects.filter(from_user=request.user.id)
        fans = UserRelation.objects.filter(to_user=request.user.id)

        if request.user.is_authenticated:
            topic_count = UserProfile.objects.get(username=request.user).topic_set.count()
            return render(request, self.template_index, {
                'topics': topics,
                'follower': follower,
                'fans': fans,
                'topic_count': topic_count
            })
        else:
            return render(request, self.template_index, {
                'topics': topics,
                'follower': follower,
                'fans': fans,
            })


class DetailView(View):
    """
    主题详情
    """

    def get(self, request, topic_id):
        topic = Topic.objects.get(id=topic_id)
        topic_comment = topic.topiccomment_set.all().order_by('-add_time')
        comment_form = CommentForm()
        return render(request, 'detail.html', {
            'topic': topic,
            'comment_form': comment_form,
            'topic_comment': topic_comment,
            'user': topic.user
        })


class PubTopicView(View):
    """
    发布主题
    """

    def get(self, request, username):
        user = UserProfile.objects.get(username=username)
        topic_form = PubTopicForm()
        return render(request, 'edit.html', {'topic_form': topic_form, 'user': user})


class CommitTopicView(View):
    """
    提交主题
    """

    def post(self, request, username):
        topic_form = PubTopicForm(request.POST)
        if topic_form.is_valid():
            topic_title = topic_form.cleaned_data['title']
            topic_content = topic_form.cleaned_data['content']
            if Topic.objects.filter(title=topic_title).exists():
                return render(request, 'edit.html', {
                    'msg': '主题已存在！',
                    'topic_form': topic_form,
                    'exists': Topic.objects.filter(title=topic_title).exists()
                })
            topic = Topic()
            user = UserProfile.objects.get(username=username)
            topic.user = user
            topic.title = topic_title
            topic.content = topic_content
            topic.save()
            return render(request, 'edit.html', {'topic_form': topic_form, 'msg': '提交成功'})
        else:
            return render(request, 'edit.html', {'msg': '输入数据有错误，请重新输入！', 'topic_form': topic_form})


class MemberView(View):
    """
    该主题所属会员
    """

    def get(self, request, username):
        member = UserProfile.objects.get(username=username)
        # 当前主题所属用户id
        topic_user_id = member.id
        # 登录用户id
        login_user_id = UserProfile.objects.get(username=request.user).id
        # 判断关注按钮状态
        global exist_rel
        global exist_inverse_rel
        exist_rel = 0
        exist_inverse_rel = 1
        if UserRelation.objects.filter(from_user=login_user_id, to_user=topic_user_id):
            exist_rel = int(UserRelation.objects.filter(from_user=login_user_id, to_user=topic_user_id)[0].rel_type)

        if UserRelation.objects.filter(from_user=topic_user_id, to_user=login_user_id):
            exist_inverse_rel = int(
                UserRelation.objects.filter(from_user=topic_user_id, to_user=login_user_id)[0].rel_type)

        return render(request, 'member.html', {
            'member': member,
            'exist_rel': exist_rel,
            'exist_inverse_rel': exist_inverse_rel,
            'topic_user_id': topic_user_id,
            'login_user_id': login_user_id
        })
