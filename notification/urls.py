from django.urls import path
# from .views import stream_notification
from .views import notifications_data,NotificationListView,notification_mark_all_read,notification_delete_all_read


urlpatterns = [
    path('notification-summary/', notifications_data, name='notification-summary'),
    path('notifications-markall/',notification_mark_all_read , name='notifications'),
    path('notifications-deleteread/',notification_delete_all_read , name='notifications_delete'),
    path('notifications/',NotificationListView.as_view() , name='notifications'),
]