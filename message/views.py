from csv_export.views import CSVExportView
from rest_framework import viewsets

from .models import Message
from .serializers import MessageSerializer


class DataExportView(CSVExportView):
    model = Message
    fields = '__all__'


class MessageViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = []
