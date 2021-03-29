from django.db import models
from message.tasks import send_mail
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Message(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField(
        'create date', default=timezone.now)
    send_date = models.DateTimeField('send date')
    body = models.TextField()
    sent = models.BooleanField(default=False)
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.title


@receiver(post_save, sender=Message)
def create_send_task(sender, instance, **kwargs):
    send_mail(instance.id, eta=instance.send_date)
