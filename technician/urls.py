from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 


router = DefaultRouter()

router.register("details", views.TechnicianDetailView, basename="account-details")


urlpatterns = [
    path('technician/', include(router.urls)),
]