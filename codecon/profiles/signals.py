from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from profiles.models import Profile


@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    """ Create a userprofile for every new user """
    print("lets create profile..")
    if created:
        Profile.objects.create(owner=instance)
