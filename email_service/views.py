from rest_framework import viewsets
from .models import EmailAccount, EmailMessage
from .serializers import EmailAccountSerializer, EmailMessageSerializer
from django.shortcuts import render


def index(request):
    return render(request, 'email_service/index.html')

class EmailAccountViewSet(viewsets.ModelViewSet):
    queryset = EmailAccount.objects.all()
    serializer_class = EmailAccountSerializer


class EmailMessageViewSet(viewsets.ModelViewSet):
    queryset = EmailMessage.objects.all().order_by('-received_at')
    serializer_class = EmailMessageSerializer