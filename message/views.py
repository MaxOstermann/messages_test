from csv_export.views import CSVExportView
from django.utils import timezone
from rest_framework import viewsets

from .models import Message
from .serializers import MessageSerializer


class DataExportView(CSVExportView):
    model = Message
    fields = '__all__'
    header = False
    specify_separator = False
    filename = 'data-export.csv'


class MessageViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = []
