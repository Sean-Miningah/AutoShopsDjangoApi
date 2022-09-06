import graphene 
from graphene_django import DjangoObjectType
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery 

from .models import AutoUser
from technician.models import TechnicianDetails
from .types import AutoUserType
from technician.types import TechnicianDetailType

class TechnicianQuery(graphene.ObjectType):
    userinfo = graphene.List(AutoUserType)
    technician = graphene.List(TechnicianDetailType)

    def resolve_userinfo(self, info, **kwargs):
        return AutoUser.objects.filter(is_technician=True,)

    def resolve_techncian(self,info, **kwargs):
        return TechnicianDetails.objects.all()

    

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.SendSecondaryEmailActivation.Field()


class Query(UserQuery, MeQuery, TechnicianQuery, graphene.ObjectType):
    pass



class Mutation(AuthMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)