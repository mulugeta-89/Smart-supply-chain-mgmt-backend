from django.urls import path
from . import views

# Defining url patterns
urlpatterns = [
    # routes for buyer
    path("buyer/register", views.BuyerCreateView.as_view(), name="buyer-create-view"),
    path("seller/register", views.SellerCreateView.as_view(), name="seller-create-view"),
    path("driver/register", views.DriverCreateView.as_view(), name="driver-create-view"),
    path("user/login", views.UserLoginView.as_view(), name="user-login-view"),
    path("product/create", views.ProductListCreateView.as_view(), name="product-list-create-view"),
    path("order/create", views.OrderCreateView.as_view(), name="order-create-api-view"),
    path('send/', views.SendMessageAPIView.as_view(), name='send-message-api-view'),
    path('inbox/', views.InboxAPIView.as_view(), name='inbox-api-view'),
    path('rate/', views.SendRatingAPIView.as_view(), name='send-message-api-view'),
    # path("product/create", views.ProductCreateView.as_view(), name="product-create-view"),
    # path("product/<int:pk>", views..as_view(), name="driver-update-destroy-view"),
]