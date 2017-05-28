from django.http import JsonResponse
from django.core import serializers
from datetime import datetime

from notifs.models import Notification


def unread(request):
    unread = request.user.notifs.filter(read_date=None)

    data = {
        "notifs" : serializers.serialize('json', unread)
    }

    return JsonResponse(data)


def mark_as_read(request, pk):
    notification = Notification.objects.get(pk=pk)
    notification.read_date = datetime.now()
    notification.save()

    data = {
        "is_marked" : True
    }

    return JsonResponse(data)
