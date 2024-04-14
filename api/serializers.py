from rest_framework import serializers
from .models import Buyer, Seller, Driver
from django.contrib.auth.hashers import make_password


# Create Buyer serializer
class BuyerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # Hide password during responses
    profile_image = serializers.ImageField(required=False)
    
    # Perform password Hashing when saved to the database
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)
    
    class Meta:
        model = Buyer
        fields = "__all__"

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
        fields = "__all__" 

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
        fields = "__all__"