from rest_framework import viewsets

# Create your views here.

from .models import (AutoUser)
from .serializers import (AutoUserSerializer)

class CreateAccountView(viewsets.ModelViewSet):
    queryset = AutoUser.objects.all()
    serializer_class = AutoUserSerializer