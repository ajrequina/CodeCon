from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from posts.models import Post

class Comment(models.Model):
    content = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now=True)
    commented_post = models.ForeignKey(Post, related_name="comments")
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.content

    class Meta:
        ordering = ['-date_created']
