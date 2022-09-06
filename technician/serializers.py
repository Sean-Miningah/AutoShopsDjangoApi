from rest_framework import serializers

from django.contrib.auth import get_user_model
AutoUser = get_user_model()

from AutoUser.serializers import AutoUserSerializer

from .models import (SkillBadge, TechnicianDetails, Specialization, 
                TechnicianSpecializations, ShopFeedbackRating, TechnicianBadge)

class TechnicianDetailsSerializer(serializers.ModelSerializer):

    autouser = AutoUserSerializer(read_only=True)

    class Meta:
        model = TechnicianDetails
        fields = '__all__'

    def create(self, validated_data):
        autouser = validated_data.pop('auto_user')
        tech_details_instance = TechnicianDetails.objects.create(**validated_data)
        return tech_details_instance

class SpecializationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Specialization
        fields = '__all__'

class TechnicianSpecializationsSerializer(serializers.ModelSerializer):

    technician = TechnicianDetailsSerializer(many=True, read_only=True)
    specialization = SpecializationSerializer(many=True, read_only=True)

    class Meta:
        model = TechnicianSpecializations
        fields = '__all__'
        depth = 1

class ShopFeedbackRatingSerializer(serializers.ModelSerializer):

    technician = TechnicianDetailsSerializer(read_only=True, many=True)
    autouser = AutoUserSerializer(read_only=True, many=True) 

    class Meta:
        model = ShopFeedbackRating
        fields = '__all__'
        depth = 2

class SkillBadgeSerializer(serializers.ModelSerializer):

    class Meta: 
        model = SkillBadge
        fields = '__all__'

class TechnicianBadgeSerializer(serializers.ModelSerializer):

    technician = TechnicianDetailsSerializer()

    class Meta: 
        model = TechnicianBadge
        fields = '__all__'
        depth = 1

class TechnicianFeedSerializer(serializers.ModelSerializer):

    tech_details = TechnicianDetailsSerializer()
    specializations = TechnicianSpecializationsSerializer()
    reviews = ShopFeedbackRatingSerializer()
    badge = TechnicianBadgeSerializer()

#  def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)