from graphene_django.types import DjangoObjectType
from .models import AutoUser


class AutoUserType(DjangoObjectType):
    class Meta: 
        model = AutoUser
        fields = '__all__'