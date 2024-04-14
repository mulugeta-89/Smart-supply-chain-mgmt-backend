from django.urls import path
from . import views

# Defining url patterns
urlpatterns = [
    # routes for buyer
    path("buyer/register", views.BuyerCreateView.as_view(), name="buyer-create-view"),
    path("buyer/<int:pk>", views.BuyerRetriveUpdateDestroyView.as_view(), name="buyer-update-destroy-view"),
    path("buyer/login", views.BuyerLoginView.as_view(), name="buyer-login-view"),
    path("buyer/logout", views.LogoutView.as_view(), name="logout-view"),

    # Routes for seller
    path("seller/register", views.SellerCreateView.as_view(), name="seller-create-view"),
    path("seller/<int:pk>", views.SellerRetriveUpdateDestroyView.as_view(), name="seller-update-destroy-view"),
    path("seller/login", views.SellerLoginView.as_view(), name="seller-login-view"),
    path("seller/logout", views.LogoutView.as_view(), name="logout-view"),

    # routes for driver
    path("driver/register", views.DriverCreateView.as_view(), name="driver-create-view"),
    path("driver/<int:pk>", views.DriverRetriveUpdateDestroyView.as_view(), name="driver-update-destroy-view"),
    path("driver/login", views.DriverLoginView.as_view(), name="driver-login-view"),
    path("driver/logout", views.LogoutView.as_view(), name="logout-view"),

]