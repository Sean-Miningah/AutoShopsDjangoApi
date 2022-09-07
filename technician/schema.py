import graphene
from graphene_django import DjangoObjectType 

from .models import SkillBadge, TechnicianDetails, TechnicianSpecializations, Specialization
from AutoUser.models import AutoUser
from .types import (TechnicianDetailType, TechnicianSpecializationsType, SpecializationType, 
        SkillBadgeType)

class AutoUserType(DjangoObjectType):

    class Meta: 
        model = AutoUser
        fields="__all__"


class TechnicianQuery(graphene.ObjectType):
    userinfo = graphene.List(AutoUserType)
    technician = graphene.List(TechnicianDetailType)
    techspecialization = graphene.List(TechnicianSpecializationsType)
    specialization = graphene.List(SpecializationType)
    skillbadge = graphene.List(SkillBadgeType)

    def resolve_skillbadge(self, info, **kwargs):
        return SkillBadge.objects.all()
    def resolve_userinfo(self, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authenticated credentials were not provided")
        return AutoUser.objects.filter(is_technician=True,)

    def resolve_technician(self,info, **kwargs):
        return TechnicianDetails.objects.all()
    
    def resolve_techspecialization(self, info, **kwargs):
        return TechnicianSpecializations.objects.all()

    def resolve_specialization(self, info, **kwargs):
        return Specialization.objects.all()


 

