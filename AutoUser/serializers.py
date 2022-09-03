from rest_framework import serializers

from django.contrib.auth import get_user_model
AutoUser = get_user_model()


class AutoUserSerializer(serializers.ModelSerializer):

    class Meta: 
        model = AutoUser
        exclude = ['is_active', 'is_staff', 'start_date']