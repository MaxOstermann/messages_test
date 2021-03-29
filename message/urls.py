from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import MessageViewSet, DataExportView

router = DefaultRouter()

router.register(r'message', MessageViewSet, basename='message')

urlpatterns = router.urls

urlpatterns += [
    path('export/', DataExportView.as_view()),
]

