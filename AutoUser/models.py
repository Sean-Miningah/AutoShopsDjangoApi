from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class CustomAccountManager(BaseUserManager):

    def create_user(self, phone_number, password, **other_fields):
        if not phone_number:
            raise ValueError("A phone number must be provided")

        user = self.model(phone_number=phone_number, **other_fields)

        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, phone_number, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(phone_number, password, **other_fields)

class AutoUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    # photo = models.ImageField(upload_to='photos/autouser/', default="default_profile_pic")
    photo=ProcessedImageField(upload_to='photos/autouser/',default="default_profile_pic", processors=[ResizeToFill(160,320, upscale=True),], format='JPEG', options={'quality': 80})
    start_date = models.DateField(auto_now=True)
    phone_number = models.CharField(max_length=50, blank=False, unique=True)
    email = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=100)
    is_technician = models.BooleanField(default=False)
    is_advertiser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name + ' ' + self.last_name

