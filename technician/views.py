from django.shortcuts import render

from django.contrib.auth import get_user_model
AutoUser = get_user_model()

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class AccountDetails(viewsets.ModelViewSet):
    pass

