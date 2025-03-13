from django.db import models
import requests
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.dispatch import receiver
import uuid
from base.emails import send_account_activation_email

class Address(BaseModel):
    address_line_1 = models.CharField(max_length=50, null=False)
    address_line_2 = models.CharField(max_length=50, null=False)
    
    zip_code = models.CharField(
        max_length=6,
        null=False,
        validators = [RegexValidator(regex=r'^\d{6}$', message='Zip code must be exactly 6 digits')]
    )
    locality = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)

    profile = models.ForeignKey(
        'Profile',
        on_delete=models.CASCADE,
        related_name='addresses',  # This creates a reverse relation
        blank=True,
        null=True
    )
    
    def save(self, *args, **kwargs):
        # Update locality, city, and state based on zip code before saving
        print("zip code is inside model   ", self.zip_code)
        # self.update_location()
        super().save(*args, **kwargs)


# class Cart(BaseModel):
#     address_line_1 = models.CharField(max_length=50, null=False)
#     address_line_2 = models.CharField(max_length=50, null=False)
    
#     zip_code = models.CharField(
#         max_length=6,
#         null=False,
#         validators = [RegexValidator(regex=r'^\d{6}$', message='Zip code must be exactly 6 digits')]
#     )
#     locality = models.CharField(max_length=100, null=True, blank=True)
#     city = models.CharField(max_length=100, null=True, blank=True)
#     state = models.CharField(max_length=100, null=True, blank=True)

#     profile = models.ForeignKey(
#         'Profile',
#         on_delete=models.CASCADE,
#         related_name='addresses',  # This creates a reverse relation
#         blank=True,
#         null=True
#     )
    
#     def save(self, *args, **kwargs):
#         # Update locality, city, and state based on zip code before saving
#         print("zip code is inside model   ", self.zip_code)
#         # self.update_location()
#         super().save(*args, **kwargs)

    
    
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=30, null=True, blank=True)
    profile_image = models.ImageField(upload_to="profile")
    
    def get_addresses(self):
        return self.addresses.all()


@receiver(post_save , sender = User)
def  send_email_token(sender , instance , created , **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            email = instance.email
            send_account_activation_email(email , email_token)
            Profile.objects.create(user = instance , email_token = email_token)

    except Exception as e:
        print("email send is failed ",e," bakwas gpt")

