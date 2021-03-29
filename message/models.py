from django.db import models
from message.tasks import send_mail


class Message(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField('create date')
    send_date = models.DateTimeField('send date')
    body = models.TextField()
    sent = models.BooleanField(default=False)
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def save(self, *args, **kwargs):
        if not self.sent:
            send_mail.apply_async(args=[self.id], eta=self.send_date)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
