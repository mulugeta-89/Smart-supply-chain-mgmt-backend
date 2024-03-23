from django.urls import path
from . import views

# Defining url patterns
urlpatterns = [
    path("buyer/create", views.BuyerCreateView.as_view(), name="buyer-create-view"),
    path("buyer/<int:pk>", views.BuyerRetriveUpdateDestroyView.as_view(), name="buyer-update-destroy-view"),
    path("seller/create", views.SellerCreateView.as_view(), name="seller-create-view"),
    path("seller/<int:pk>", views.SellerRetriveUpdateDestroyView.as_view(), name="seller-update-destroy-view"),
    path("driver/create", views.DriverCreateView.as_view(), name="driver-create-view"),
    path("driver/<int:pk>", views.DriverRetriveUpdateDestroyView.as_view(), name="driver-update-destroy-view")
]