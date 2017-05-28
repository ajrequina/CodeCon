from django.http import JsonResponse
from django.core import serializers

from notifications.models import Notification

def notifications(request):
    notifs = serializers.serialize('json', request.user.notifications.unread())
    data = {
        "notifications" : notifs
    }

    return JsonResponse(data)


def mark_as_read(request, pk):
    notification = Notification.objects.get(pk=pk)
    notification.mark_as_read()

    data = {
        "is_marked" : True
    }

    return JsonResponse(data)

