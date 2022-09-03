from django.contrib.auth import get_user_model
AutoUser = get_user_model()

from django.db import models


class TechnicianDetails(models.Model):
    autouser_id = models.ForeignKey(AutoUser, on_delete=models.CASCADE)
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
    technician = models.ManyToManyField(TechnicianDetails)
    specialization = models.ManyToManyField(Specialization)


class ShopFeedbackRating(models.Model):
    technician_id = models.ForeignKey(TechnicianDetails, 
            null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    rating = models.FloatField()
    autouser = models.ForeignKey(AutoUser, null=True, 
            on_delete=models.SET_NULL)

class SkillBadge(models.Model):
    BADGE_OPTIONS = (
        ('gold', 'GOLD'),
        ('silver', 'SILVER'),
        ('bronze', 'BRONZE')
    )
    badge = models.CharField(max_length=20, choices=BADGE_OPTIONS)

class TechnicinanBadge(models.Model):
    
    badge = models.ForeignKey(SkillBadge, on_delete=models.CASCADE)
    technician_id = models.ForeignKey(TechnicianDetails, on_delete=models.CASCADE) 