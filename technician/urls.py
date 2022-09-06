from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 


router = DefaultRouter()

router.register("details", views.TechnicianDetailView, basename="account-details")
router.register("specializations", views.SpecializationView, basename="specializations")
router.register("feed", views.TechnicianFeedView, basename="technician-feed")

urlpatterns = [
    path('technician/', include(router.urls)),
]