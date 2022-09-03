from rest_framework import serializers

from django.contrib.auth import get_user_model
AutoUser = get_user_model()

from .models import (SkillBadge, TechnicianDetails, Specialization, 
                TechnicianSpecializaitons, ShopFeedbackRating, TechnicinanBadge)

class TechnicianDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TechnicianDetails
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Specialization
        fields = '__all__'

class TechnicianSpecializationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TechnicianSpecializaitons
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
        model = TechnicinanBadge
        fields = '__all__'
        depth = 1