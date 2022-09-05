import graphene
from graphene_django import DjangoObjectType 

from .models import TechnicianDetails, Specialization
from AutoUser.models import AutoUser

class AutoUserType(DjangoObjectType):

    class Meta: 
        model = AutoUser
        fields="__all__"

class TechnicianDetailsType(DjangoObjectType):

    class Meta:
        model = TechnicianDetails
        fields = ("id", 'autouser', 'lat', 'lng', 
                'profile_picture', 'shop_description', 'shop_goal', 'rating') # the fields that we want to contain in this text




class Query(graphene.ObjectType):
    all_techniciandetails = graphene.List(TechnicianDetailsType)
    
    def resolve_all_techniciandetails(root, info):
        return TechnicianDetails.objects.all()

 

    

schema = graphene.Schema(query=Query)
