from django.db import models
from Accounts.models import User

# Create your models here.
class Notification(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='notifications')
    message=models.TextField()
    is_read=models.BooleanField(default=False)
    delivered=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
