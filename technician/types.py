from graphene_django.types import DjangoObjectType
from .models import TechnicianDetails, TechnicianSpecializations, Specialization


class TechnicianDetailType(DjangoObjectType):
    class Meta: 
        model = TechnicianDetails
        fields = '__all__'

class TechnicianSpecializationsType(DjangoObjectType):

    class Meta:
        model = TechnicianSpecializations
        filds = "__all__"

class SpecializationType(DjangoObjectType):
    class Meta:
        model = Specialization
        fields = '__all__'
