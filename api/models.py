from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add fields common to all user types
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    registration_date = models.DateTimeField(auto_now_add=True)
    rating_value = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    payment_method = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    # Add other common fields as needed
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)

class BaseProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    class Meta:
        abstract = True  # Set abstract to True to prevent Django from creating a table for this model

class BuyerProfile(BaseProfile):
    pass

class SellerProfile(BaseProfile):
    tax_number = models.CharField(max_length=100)

class DriverProfile(BaseProfile):
    license_number = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)

class Product(models.Model):
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)  # Define the relationship
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    quantity = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Products/', null=True, blank=True)
    product_type = models.CharField(max_length=200)
