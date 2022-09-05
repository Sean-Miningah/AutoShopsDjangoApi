from django.shortcuts import render

from django.contrib.auth import get_user_model
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


        # listing technician details, updating technician details, 
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None: 
            serializer = self.get_serializer(page, many=True)
            return self.paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


