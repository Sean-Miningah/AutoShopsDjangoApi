import random
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import api_view

# Create your views here.

from .models import (AutoUser)
from .serializers import (AutoUserSerializer)


@api_view(['POST'])
def verifyemail(request):
    useremail = request.data['email']

    subject = "Verification Message"
    message =  str(random.randrange(1000, 10000))
    
    send_mail(subject, message, 
        settings.DEFAULT_FROM_EMAIL, [useremail,])

    res = {
        "verification-code": message,
    }

    return Response(res, status=status.HTTP_200_OK)


class CreateAccountView(viewsets.ModelViewSet):
    queryset = AutoUser.objects.all()
    serializer_class = AutoUserSerializer