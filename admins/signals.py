from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Topic,TopicContent



@receiver(post_save,sender=Topic)
def create_content_on_topic_create(instance,created,**kwargs):
    if created:
        TopicContent.objects.create(topic=instance)



