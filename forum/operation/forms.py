#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Suger'
__date__ = '2018/7/29 上午1:10'

from django import forms


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)