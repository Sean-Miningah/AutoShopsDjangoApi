from django.contrib.auth import get_user_model
AutoUser = get_user_model()

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class TechnicianDetails(models.Model):
    autouser = models.ForeignKey(AutoUser, on_delete=models.CASCADE) # should implement a an optional one to one relation with the auto user
    lat = models.CharField(max_length=30, blank=True)
    lng = models.CharField(max_length=30, blank=True)
    # profile_picture = models.ImageField(upload_to='photos/technician/')
    profile_picture=ProcessedImageField(upload_to='photos/autouser/', default='default_technician_photo',
        processors=[ResizeToFill(160,320, upscale=True)], format='JPEG', options={'quality': 80})
    shop_description = models.TextField()
    shop_goal = models.TextField()
    rating = models.FloatField(default=0)

    def __str__(self):
        return str(self.id) + ' -- name is ' + str(self.autouser)

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

    def __str__(self):
        return self.name

class TechnicianSpecializations(models.Model):
    technician = models.ManyToManyField(TechnicianDetails, blank = True)
    specialization = models.ManyToManyField(Specialization, blank=True)


class ShopFeedbackRating(models.Model):
    technician = models.ForeignKey(TechnicianDetails, 
            null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    rating = models.FloatField()
    date = models.DateField(auto_now=True)
    autouser = models.ForeignKey(AutoUser, null=True, 
            on_delete=models.SET_NULL)

    def __str__(self):
        return self.date

class SkillBadge(models.Model):
    BADGE_OPTIONS = (
        ('gold', 'GOLD'),
        ('silver', 'SILVER'),
        ('bronze', 'BRONZE')
    )
    badge = models.CharField(max_length=20, choices=BADGE_OPTIONS)

    def __str__(self):
        return self.badge

class TechnicianBadge(models.Model):
    
    badge = models.ForeignKey(SkillBadge, on_delete=models.CASCADE)
    technician = models.ForeignKey(TechnicianDetails, on_delete=models.CASCADE) 

    def __str__(self):
        return self.technician + self.badge