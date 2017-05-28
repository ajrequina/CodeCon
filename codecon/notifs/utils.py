from notifs.models import Notification


def notify_followers(user, verb, target_object, page_type):
    description = "@" + user.username + " " + \
                  verb + " " + str(target_object)
    actor = user

    for receiver in user.followers.all():
        Notification.objects.create(
            receiver=receiver.follower,
            description=description,
            target_pk=target_object.pk,
            page_type=page_type,
            actor=actor
            )


def notify_owner(receiver, actor, verb, target_object, page_type):
    if receiver != actor:
        description = "@" + actor.username + " " + \
                      verb + " " + str(target_object)

        Notification.objects.create(
            receiver=receiver,
            description=description,
            target_pk=target_object.pk,
            page_type=page_type,
            actor=actor
            )
