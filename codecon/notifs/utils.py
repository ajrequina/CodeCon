from notifs.models import Notification


def notify_followers(user, verb, target_object, page_type):
    description = "@" + user.username + " " + \
                  verb + " " + str(target_object)
    actor = user
    link = "#"
    if page_type == "post":
        link = "/post/detail/" + str(target_object.pk) + "/"
    elif page_type == "profile":
        link = "/post/profile/" + str(target_object.pk) + "/"

    for receiver in user.followers.all():
        Notification.objects.create(
            receiver=receiver.follower,
            description=description,
            target_link=link,
            page_type=page_type,
            actor=actor
            )


def notify_owner(receiver, actor, verb, target_object, page_type):
    if receiver != actor:
        description = "@" + actor.username + " " + \
                      verb + " " + str(target_object)

        link = "#"
        if page_type == "post":
            link = "/post/detail/" + str(target_object.pk) + "/"
        elif page_type == "profile":
            link = "/post/profile/" + str(target_object.pk) + "/"

        Notification.objects.create(
            receiver=receiver,
            description=description,
            target_link=link,
            page_type=page_type,
            actor=actor
            )
