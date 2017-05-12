from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from posts import models

admin.site.register(models.Post, MarkdownModelAdmin)
admin.site.register(models.Like)
admin.site.register(models.Comment)
admin.site.register(models.FileUpload)