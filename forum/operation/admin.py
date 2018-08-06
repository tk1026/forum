from django.contrib import admin

from .models import TopicComment, UserFavorite, UserRelation

admin.site.register(TopicComment)
admin.site.register(UserFavorite)
admin.site.register(UserRelation)