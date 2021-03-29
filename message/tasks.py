from MessageTest.celery import app
from django.apps import apps


@app.task
def send_mail(id):
    Message = apps.get_model('message.Message')
    message = Message.objects.filter(id=id)
    message.sent = True
    message.save()
