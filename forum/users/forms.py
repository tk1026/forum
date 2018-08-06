#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Suger'
__date__ = '2018/7/26 上午12:14'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=5, max_length=16, error_messages={
        'required': u'请输入用户名',
        'min_length': u'用户名最少5个字符',
        'max_length': u'用户名最多16个字符'
    })
    password = forms.CharField(required=True, min_length=8, max_length=20, error_messages={
        'required': u'请输入密码',
        'min_length': u'密码最少8个字符',
        'max_length': u'密码最多20个字符'
    } )


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, initial='UserName', min_length=5, max_length=16, error_messages={
        'required': u'请输入用户名',
        'min_length': u'用户名最少5个字符',
        'max_length': u'用户名最多16个字符'
    })
    email = forms.EmailField(required=True, initial='YouEmail@Gmail.com', error_messages={
        'required': u'请输入邮箱',
        'invalid': u'请输入正确的邮箱地址'
    })
    password = forms.CharField(required=True, min_length=8, max_length=20, error_messages={
        'required': u'请输入密码',
        'min_length': u'密码最少8个字符',
        'max_length': u'密码最多20个字符'
    })


class ModifyInfoForm(forms.Form):
    nick_name = forms.CharField(max_length=20)
    mobile = forms.CharField(max_length=11)
    email = forms.EmailField()


