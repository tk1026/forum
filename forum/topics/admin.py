from django.contrib import admin

from .models import Topic, TopicTag


admin.site.register(Topic)
admin.site.register((TopicTag))