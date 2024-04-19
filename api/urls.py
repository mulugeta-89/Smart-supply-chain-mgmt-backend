from django.urls import path
from . import views

# Defining url patterns
urlpatterns = [
    # routes for buyer
    path("buyer/register", views.BuyerCreateView.as_view(), name="buyer-create-view"),
    path("seller/register", views.SellerCreateView.as_view(), name="seller-create-view"),
    path("driver/register", views.DriverCreateView.as_view(), name="driver-create-view")

    # path("product/create", views.ProductCreateView.as_view(), name="product-create-view"),
    # path("product/<int:pk>", views..as_view(), name="driver-update-destroy-view"),
]