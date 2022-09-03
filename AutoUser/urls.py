from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 


router = DefaultRouter()
router.register("create-account", views.CreateAccountView, basename="create-account")


urlpatterns = [
    path('auto-user/', include(router.urls)),
]