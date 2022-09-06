from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model

import technician
AutoUser = get_user_model()

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import ( TechnicianDetails, Specialization, TechnicianSpecializations,
                ShopFeedbackRating, SkillBadge, TechnicianBadge)
from .serializers import ( TechnicianDetailsSerializer, SpecializationSerializer, TechnicianSpecializationsSerializer,
                ShopFeedbackRatingSerializer, SkillBadgeSerializer, TechnicianBadgeSerializer)


class TechnicianDetailView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TechnicianDetailsSerializer
    
    def get_queryset(self):
        user = self.request.user
        return TechnicianDetails.objects.filter(autouser=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        res = {
            "message": "Details Entered Successfully!!",
        }

        return Response(res, status=status.HTTP_201_CREATED, headers=headers)


        ## Endpoint to provide technician with information on self

    #     return Response(serializer.data)

class TechnicianFeedView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TechnicianDetailsSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category', 'in_stock']
    
    def get_queryset(self):
        user = self.request.user
        return TechnicianDetails.objects.exclude(autouser=user)

    def list(self, request, *args, **kwargs):
        res = []
        tech_autouser = AutoUser.objects.filter(is_technician=True)
        for tech in TechnicianDetails.objects.filter(autouser__in=tech_autouser):
            # print(TechnicianSpecializationsSerializer(data=TechnicianSpecializations.
            #                 objects.filter(technician=tech)[0]))
            # specialization = TechnicianSpecializationsSerializer(data=TechnicianSpecializations.
            #                 objects.filter(technician=tech), many=True)
            # print(specialization[0])
            specialization = TechnicianSpecializations.objects.filter(technician=tech)
            # print(help(specialization))
            reviews = ShopFeedbackRatingSerializer(data=ShopFeedbackRating.objects.filter(technician=tech), 
                            many=True).is_valid(raise_exception=True)
            badge = TechnicianBadgeSerializer(data=TechnicianBadge.objects.filter(technician=tech)).is_valid(raise_exception=True)
            tech_info = {
                # "specializations": specialization.validated_data,
                "reviews": reviews.validated_data,
                "badge": badge.validated_data
            }
            res.append(tech_info)

        return Response(res,status=status.HTTP_200_OK)

class SpecializationView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = SpecializationSerializer
    queryset =  Specialization.objects.all()  
    http_method_names = ['get']

    # def create(self, request, *args, **kwargs):
    #     pass 

    # def update(self, request, *args, **kwargs):
    #     pass





