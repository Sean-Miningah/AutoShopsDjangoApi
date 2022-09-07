import random
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.mixins import LoginRequiredMixin 
from graphene_django.views import GraphQLView


from .models import (AutoUser)
from .serializers import (AutoUserSerializer)


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Acquire instance of created user
        theUser = AutoUser.objects.get(email=request.data['email'])


        token = Token.objects.create(user=theUser)

        res = {
            "message": "Succesfully Registered!",
            "token": "Token " + token.key
        }

        return Response(res, status=status.HTTP_201_CREATED, headers=headers)
