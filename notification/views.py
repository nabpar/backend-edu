from django.http import JsonResponse, StreamingHttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from rest_framework import generics,permissions,response
from rest_framework.decorators import api_view,permission_classes
import json
import time
from django.shortcuts import get_object_or_404

from .models import Notification
from Accounts.models import User
from .serialzier import NotificationSerializer
from EduAid.pagination import PageNumberPagination


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def notifications_data(request):
    query=Notification.objects.filter(user=request.user)
    if query.exists():
        unread_notifications = query.filter(is_read=False).count()
        latest_notifications = query.order_by('-created_at')[:5]
        serializer = NotificationSerializer(latest_notifications, many=True)
        data = {
            'unread_notifications': unread_notifications,
            'latest_notifications': serializer.data
        }
    else:
        data = {
                'unread_notifications': 0,
                'latest_notifications': []
            }
    return response.Response(data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def notification_mark_all_read(request):
    query=Notification.objects.filter(user=request.user,is_read=False)
    if query.exists():
        query.update(is_read=True)
        
    return response.Response({
        'message':'Marked all as read'
    })


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def notification_delete_all_read(request):
    notifications_to_delete = Notification.objects.filter(user=request.user, is_read=True)
    notifications_to_delete_count = notifications_to_delete.count()
    notifications_to_delete.delete()

    return response.Response({
        'message': f'Deleted {notifications_to_delete_count} read notifications.'
    })




class NotificationListView(generics.ListCreateAPIView):
    serializer_class=NotificationSerializer
    permission_classes=[permissions.IsAuthenticated]
    queryset=Notification.objects.all()
    # pagination_class=PageNumberPagination

    def get_queryset(self):
        queryset= super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user).order_by('-created_at')
        return queryset