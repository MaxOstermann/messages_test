from MessageTest.celery import app
from django.apps import apps


@app.task
def send_mail(*args, **kwargs):
    Message = apps.get_model('message.Message')
    Message.objects.filter(id=args[0])\
        .update(sent=True)
