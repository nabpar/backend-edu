from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    user_name=serializers.SerializerMethodField()
    
    def get_user_name(self,obj):
        return obj.user.name
    
    class Meta:
        model=Notification
        fields='__all__'
        
