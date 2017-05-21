from django.contrib import admin

from profiles.models import Profile, Follow


admin.site.register(Profile)
admin.site.register(Follow)
