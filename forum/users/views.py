# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from .forms import LoginForm, RegisterForm, ModifyInfoForm
from .models import UserProfile
from operation.models import UserFavorite, UserRelation
from topics.models import Topic


class LoginView(View):
    """
    用户登录
    """
    template_index = 'index.html'
    template_login = 'login.html'

    def get(self, request):
        return render(request, self.template_login, {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            pass_word = login_form.cleaned_data['password']
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return redirect(to='topic:index')
            else:
                return render(request, self.template_login, {'login_form': login_form, 'msg': '用户名或密码错误！'})
        else:
            return render(request, self.template_login, {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect(to='topic:index')


class RegisterView(View):
    """
    用户注册
    """

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = register_form.cleaned_data['username']
            if UserProfile.objects.filter(username=user_name):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '用户名已存在'})
            user_email = register_form.cleaned_data.get('email')
            pass_word = register_form.cleaned_data.get('password')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_email
            user_profile.password = make_password(pass_word)
            user_profile.save()
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


class FavTopicView(View):
    """
    用户收藏主题展示
    """

    def get(self, request):
        username = request.user
        user = UserProfile.objects.get(username=username)
        fav_topic_list = UserFavorite.objects.filter(user=user)
        topic_id_list = fav_topic_list.values_list('fav_id', flat=True)
        # 主题列表生成器
        topic_list = [Topic.objects.get(id=topic_id) for topic_id in topic_id_list]
        # topic_list = [Topic.objects.get(id=fav_topic.fav_id) for fav_topic in fav_topic_list]
        return render(request, 'fav-topic.html', {
            'topic_list': topic_list,
        })


class UserFollowerView(View):
    """
    用户关注
    """

    def get(self, request):
        rel_obj_list = UserRelation.objects.filter(from_user=request.user.id)
        if rel_obj_list:
            follower_list = [UserProfile.objects.get(id=rel_obj.to_user) for rel_obj in rel_obj_list]
            return render(request, 'follower.html', {'follower_list': follower_list})
        else:
            return render(request, 'follower.html')


class UserFansView(View):
    """
    用户粉丝
    """

    def get(self, request):
        rel_obj_list = UserRelation.objects.filter(to_user=request.user.id)
        if rel_obj_list:
            fans_list = [UserProfile.objects.get(id=rel_obj.from_user) for rel_obj in rel_obj_list]
            return render(request, 'fans.html', {'fans_list': fans_list})
        else:
            return render(request, 'fans.html')


class UserCenterView(View):
    """
    用户中心
    """

    def get(self, request):
        return render(request, 'user-center.html')


class ModifyInfoView(View):
    """
    修改用户基本信息
    """
    def get(self, request):
        return render(request, 'user-center.html')

    def post(self, request):
        user_info = ModifyInfoForm(request.POST)
        if user_info.is_valid():
            request.user.nick_name = user_info.cleaned_data['nick_name']
            request.user.email = user_info.cleaned_data['email']
            request.user.mobile = user_info.cleaned_data['mobile']
            request.user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')