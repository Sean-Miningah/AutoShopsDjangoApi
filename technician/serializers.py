from rest_framework import serializers

from django.contrib.auth import get_user_model
AutoUser = get_user_model()

from AutoUser.serializers import AutoUserSerializer

from .models import (SkillBadge, TechnicianDetails, Specialization, 
                TechnicianSpecializations, ShopFeedbackRating, TechnicianBadge)

class TechnicianDetailsSerializer(serializers.ModelSerializer):

    autouser = AutoUserSerializer()

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

    class Meta:
        model = TechnicianSpecializations
        fields = '__all__'
        depth = 1

class ShopFeedbackRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopFeedbackRating
        fields = '__all__'
        depth = 1

class SkillBadgeSerializer(serializers.ModelSerializer):

    class Meta: 
        model = SkillBadge
        fields = '__all__'

class TechnicianBadgeSerializer(serializers.ModelSerializer):

    class Meta: 
        model = TechnicianBadge
        fields = '__all__'
        depth = 1