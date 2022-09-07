import graphene
from graphene_django import DjangoObjectType 

from .models import (SkillBadge, TechnicianDetails, TechnicianSpecializations, Specialization,
        ShopFeedbackRating)
from AutoUser.models import AutoUser
from .types import (TechnicianDetailType, TechnicianSpecializationsType, SpecializationType, 
        SkillBadgeType, ShopFeedbackRatingType)

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

# Mutations
class FeedbackInput(graphene.InputObjectType):
    id = graphene.ID()
    tech_id = graphene.ID()
    description = graphene.String()
    rating = graphene.Float()


class CreateFeedback(graphene.Mutation):
    class Arguments:
        feedback_data = FeedbackInput(required=True)

    feedback = graphene.Field(ShopFeedbackRatingType)

    def mutate(root, info, feedback_data=None):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authenticated credentials were not provided")

        tech = TechnicianDetails.objects.get(id=feedback_data.tech_id)
        feedback_instance = ShopFeedbackRating(
            technician=tech, description=feedback_data.description,
            rating=feedback_data.rating, 
            autouser=user
        )
        feedback_instance.save()
        return CreateFeedback(feedback=feedback_instance)
        
class UpdateFeedback(graphene.Mutation):
    class Arguments:
        feedback_data = FeedbackInput(required=True)

    feedback = graphene.Field(ShopFeedbackRatingType)

    def mutate(root, info, feedback_data=None):
        feedback_instance = ShopFeedbackRating.objects.get(pk=feedback_data.id)

        if feedback_instance:
            feedback_instance.tech_id=feedback_data.tech_id
            feedback_instance.description=feedback_data.description
            feedback_instance.rating=feedback_data.rating
            feedback_instance.save()
            return UpdateFeedback(feedback=feedback_instance)
        return UpdateFeedback(book=None)

class DeleteFeedback(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    feedback = graphene.Field(ShopFeedbackRatingType)

    def mutate(root, info, id):
        feedback_instance = ShopFeedbackRating.objects.get(pk=id)
        feedback_instance.delete()

        return None

 

class TechMutations(graphene.ObjectType):
    create_feedback = CreateFeedback.Field()
    update_feedback = UpdateFeedback.Field()
    delete_feedback = DeleteFeedback.Field()