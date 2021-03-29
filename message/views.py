from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = []
