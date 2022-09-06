from graphene_django.types import DjangoObjectType
from .models import TechnicianDetails


class TechnicianDetailType(DjangoObjectType):
    class Meta: 
        model = TechnicianDetails
        fields = '__all__'