from django.shortcuts import render

from .models import Notification


def notifications(request):

    notifications_list = Notification.objects.filter(user=request.user)

    return render(request, 'notifications/notifications.html', {'notifications': notifications_list})
