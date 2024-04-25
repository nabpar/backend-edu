from django.db.models.signals import post_save,post_delete
from admins.models import TopicContent,Topic,Category,ContactLeads
from .models import Notification
from django.dispatch import receiver
from Accounts.models import User


@receiver(post_save,sender=TopicContent)
def notify_on_new_content(instance,created,**kwargs):
    if created:
        if instance.status=='DRAFT':
            Notification.objects.create(user=instance.topic.assign_to,message=f'You are assigned a new topic `{instance.topic.name}`')


@receiver(post_save,sender=TopicContent)
def notify_admin_on_review(instance,created,**kwargs):
    if instance.status=='REVIEW':
        admin_users = User.objects.filter(role='ADMIN')
        for admin_user in admin_users:
            Notification.objects.create(user=admin_user,message=f'New topic added for review `{instance.topic.name}` by `{instance.topic.assign_to.name}`')

    if instance.status=='REJECTED':
        Notification.objects.create(user=instance.topic.assign_to,message=f'Bad news the topic {instance.topic.name} was rejected with message: {instance.status_message}')


    if instance.status=='PUBLISHED':
        students = User.objects.filter(role='STUDENT')
        Notification.objects.create(user=instance.topic.assign_to,message=f'Congrats the topic {instance.topic.name} was approved and published by admin.')
        for stu in students:
            Notification.objects.create(user=stu,message=f'Checkout the new topic {instance.topic.name} under {instance.topic.category.name} > {instance.topic.subject.name}')



@receiver(post_delete,sender=Topic)
def notify_of_delete(instance,**kwargs):
    users=User.objects.filter(role__in=["STUDENT","TEACHER"])
    for user in users:
        Notification.objects.create(user=user,message=f'The topic `{instance.name} is no longer available`')
