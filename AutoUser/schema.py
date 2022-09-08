import graphene 
from graphene_django import DjangoObjectType
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery 

from .models import AutoUser, AutoUserFavourite
from technician.models import TechnicianDetails, TechnicianSpecializations, Specialization
from .types import AutoUserFavouriteType, AutoUserType
from technician.types import TechnicianDetailType, TechnicianSpecializationsType, SpecializationType

class AutoUserQuery(graphene.ObjectType):
    autouser = graphene.List(AutoUserType)

class AutoUserFavouriteQuery(graphene.ObjectType):
    favourites = graphene.List(AutoUserFavouriteType)

    def resolve_favourites(root, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authenticated credentials were not provided")
        return AutoUserFavourite.objects.filter(auto_user=user)

class FavouriteInput(graphene.InputObjectType):
    id = graphene.ID()
    auto_user = graphene.ID()
    tech_id = graphene.ID()


class FavouriteTech(graphene.Mutation):
    class Arguments:
        favourite_data = FavouriteInput(required=True) 
    
    favourite = graphene.Field(AutoUserFavouriteType)

    def mutate(root, info, favourite_data=None):

        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authenticated credentials required")

        tech = AutoUser.objects.get(id=favourite_data.tech_id, is_technician=True )
        # Search for pre-existing relationship 
        if_favoured = AutoUserFavourite.objects.filter(auto_user=user, technician=tech).exists()
        if if_favoured:
            raise Exception("Relationship already exists.")

        favourite_instance = AutoUserFavourite(
            auto_user = user, technician=tech, 
        )
        favourite_instance.save()
        return FavouriteTech(favourite=favourite_instance)


class AutoUserMutations(graphene.ObjectType):
    favourite_tech = FavouriteTech.Field()
    # technician = graphene.List(TechnicianDetailType)
    # techspecialization = graphene.List(TechnicianSpecializationsType)
    # specialization = graphene.List(SpecializationType)

    # def resolve_userinfo(self, info, **kwargs):
    #     return AutoUser.objects.filter(is_technician=True,)

    # def resolve_technician(self,info, **kwargs):
    #     return TechnicianDetails.objects.all()
    
    # def resolve_techspecialization(self, info, **kwargs):
    #     return TechnicianSpecializations.objects.all()

    # def resolve_specialization(self, info, **kwargs):
    #     return Specialization.objects.all()

    

# class AuthMutation(graphene.ObjectType):
#     register = mutations.Register.Field()
#     verify_account = mutations.VerifyAccount.Field()
#     token_auth = mutations.ObtainJSONWebToken.Field()
#     update_account = mutations.UpdateAccount.Field()
#     resend_activation_email = mutations.SendSecondaryEmailActivation.Field()


# class Query(UserQuery, MeQuery, TechnicianQuery, graphene.ObjectType):
#     pass



# class Mutation(AuthMutation, graphene.ObjectType):
    pass

# schema = graphene.Schema(query=Query, mutation=Mutation)