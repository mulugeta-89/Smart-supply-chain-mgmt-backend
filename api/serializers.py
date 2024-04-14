from rest_framework import serializers
from .models import Buyer, Seller, Driver
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

# Create Buyer serializer
class BuyerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # Hide password during responses
    profile_image = serializers.ImageField(required=False)
        
    class Meta:
        model = Buyer
        fields = ['username', "password", 'email', 'first_name', 'last_name', "profile_image", 'phone_number', 'address', 'registration_date','payment_method', 'rating_value']

    # Perform password Hashing when saved to the database
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)

# Create Seller serializer
class SellerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # Hide password during responses
    profile_image = serializers.ImageField(required=False)

    # Perform password Hashing when saved to the database
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)
    
    class Meta:
        model = Seller
        fields = ["username", "password", 'email', 'first_name', 'last_name', "phone_number", "address", "registration_date", "profile_image", "account_number", "rating_value", "tax_number"]

# Create Driver serializer
class DriverSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # Hide password during responses
    profile_image = serializers.ImageField(required=False)

    # Perform password Hashing when saved to the database
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)
    
    class Meta:
        model = Driver
        fields = ["username", "password", 'email', 'first_name', 'last_name', "phone_number", "address", "registration_date", "profile_image", "account_number", "rating_value", "license_number", "car_model"]