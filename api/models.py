from django.db import models
from django.contrib.auth.models import AbstractUser

# Create model for Buyer
class Buyer(AbstractUser):

    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='buyers/profile_images/', null=True, blank=True)
    acct_type = models.CharField(max_length=100, default="Buyer")
    rating_value = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        # Set constant value for acct_type
        self.acct_type = "Buyer"
        super().save(*args, **kwargs)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='buyer_groups',
        blank=True,
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='buyer_user_permissions',
        blank=True,
        verbose_name='user permissions'
    )

    # Specifying table for Buyer Model
    class Meta:
        db_table = "buyer"

    def __str__(self):
        return self.username

# Create model for Seller
class Seller(AbstractUser):

    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    account_number = models.CharField(max_length=50)
    rating_value = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    profile_image = models.ImageField(upload_to='sellers/profile_images/', null=True, blank=True)
    acct_type = models.CharField(max_length=100, default="Seller")
    tax_number = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Set constant value for acct_type
        self.acct_type = "Seller"
        super().save(*args, **kwargs)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='seller_groups',
        blank=True,
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='seller_user_permissions',
        blank=True,
        verbose_name='user permissions'
    )

    # Specifying table for Buyer Model
    class Meta:
        db_table = "seller"

    def __str__(self):
        return self.username
    
# Create model for Driver
class Driver(AbstractUser):

    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    account_number = models.CharField(max_length=50)
    rating_value = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    license_number = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='drivers/profile_images/', null=True, blank=True)
    acct_type = models.CharField(max_length=100, default="Driver")
    car_model = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Set constant value for acct_type
        self.acct_type = "Driver"
        super().save(*args, **kwargs)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='driver_groups',
        blank=True,
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='driver_user_permissions',
        blank=True,
        verbose_name='user permissions'
    )

    # Specifying table for Buyer Model
    class Meta:
        db_table = "driver"

    def __str__(self):
        return self.username