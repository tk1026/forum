#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Suger'
__date__ = '2018/7/28 上午1:39'

from django import forms


class PubTopicForm(forms.Form):
    title = forms.CharField(required=True, max_length=36, error_messages={
        'required': '请输入标题名', 'max_length': '名称最多36个字符'
    })
    content = forms.CharField(widget=forms.Textarea)