from django.db import models

# Create model for Buyer
class Buyer(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='buyers/profile_images/', null=True, blank=True)
    rating_value = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    # Specifying table for Buyer Model
    class Meta:
        db_table = "buyer"

    def __str__(self):
        return self.username

# Create model for Seller
class Seller(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    account_number = models.CharField(max_length=50)
    rating_value = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    profile_image = models.ImageField(upload_to='sellers/profile_images/', null=True, blank=True)
    tax_number = models.CharField(max_length=100)

    # Specifying table for Seller Model
    class Meta:
        db_table = "seller"

    def __str__(self):
        return self.username
    
# Create model for Driver
class Driver(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    account_number = models.CharField(max_length=50)
    rating_value = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    license_number = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='drivers/profile_images/', null=True, blank=True)
    car_model = models.CharField(max_length=100)

    # Specifying table for Driver Model
    class Meta:
        db_table = "driver"
    
    def __str__(self):
        return self.username