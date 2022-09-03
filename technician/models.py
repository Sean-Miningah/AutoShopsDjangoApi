from django.contrib.auth import get_user_model
AutoUser = get_user_model()

from django.db import models


class Technician(models.Model):
    lat = models.CharField(max_length=30, blank=True)
    lng = models.CharField(max_length=30, blank=True)
    profile_picture = models.ImageField(upload_to='user/technician/')
    shop_description = models.TextField()
    shop_goal = models.TextField()
    rating = models.FloatField()

class Specialization(models.Model):
    SPECIALIZATIONS_OPTIONS = (
        ('service technician', 'SERVICE TECHNICIAN'),
        ('diagnostic technician', 'DIAGNOSTIC TECHNICIAN'),
        ('vehicle refinisher', 'VEHICLE REFINISHER'),
        ('body repair technician', 'BODY REPAIR TECHNICIAN'),
        ('vehicle inspector', 'VEHICLE INSPECTOR'),
        ('brake and transmission technician', 'BRAKE AND TRANSMISSION TECHNICIAN'),
    )
    name = models.CharField(max_length=40, choices=SPECIALIZATIONS_OPTIONS)

class TechnicianSpecializaitons(models.Model):
    technician = models.ManyToManyField(Technician)
    specialization = models.ManyToManyField(Specialization)


class ShopFeedbackRating(models.Model):
    technician_id = models.ForeignKey(Technician)
    description = models.TextField()
    rating = models.FloatField()
    autouser = models.ForeignKey(AutoUser)


class ShopBadge(models.Model):
    BADGE_OPTIONS = (
        ('gold', 'GOLD'),
        ('silver', 'SILVER'),
        ('bronze', 'BRONZE')
    )
    name = models.CharField(max_length=20, choices=BADGE_OPTIONS)
    technician_id = models.ForeignKey(Technician)