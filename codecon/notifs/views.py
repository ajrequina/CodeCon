from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime

from notifs.models import Notification


def unread(request):
    unread = request.user.notifs.filter(read_date=None)
    return render(request, 'notifs.html', {'notifs': unread})


def mark_as_read(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    notification.read_date = datetime.now()
    notification.save()

    data = {
        "is_marked" : True
    }

    return JsonResponse(data)


def notif_link(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    notification.read_date = datetime.now()
    notification.save()

    return redirect(notification.target_link)
