from django.urls import path
from . import views

# Defining url patterns
urlpatterns = [
    # routes for buyer
    path("buyer/register", views.BuyerCreateView.as_view(), name="buyer-create-view"),
    path("seller/register", views.SellerCreateView.as_view(), name="seller-create-view"),
    path("driver/register", views.DriverCreateView.as_view(), name="driver-create-view"),
    path("user/login", views.UserLoginView.as_view(), name="user-login-view"),

    # endpoint for order
    path("order/create", views.OrderCreateView.as_view(), name="order-create-api-view"),

    # endpoint related to messages
    path('send/', views.SendMessageAPIView.as_view(), name='send-message-api-view'),
    path('inbox/', views.InboxAPIView.as_view(), name='inbox-api-view'),
    path("message/<int:pk>/update", views.MessageUpdateView.as_view(), name="message-update-view"),

    # endpoint related to rating
    path('rate/', views.SendRatingAPIView.as_view(), name='send-message-api-view'),

    # endpoints related to product
    path("product/create", views.ProductCreateView.as_view(), name="product-create-view"),
    path("products", views.ProductListView.as_view(), name="product-list-create-view"),
    path("product/<int:pk>", views.ProductRetrieveView.as_view(), name="product-retrieve-view"),
    path("product/<int:pk>/update", views.ProductUpdateView.as_view(), name="product-update-view"),
    path("product/<int:pk>/destroy", views.ProductDestroyView.as_view(), name="product-destroy-view")
    # path("product/create", views.ProductCreateView.as_view(), name="product-create-view"),
]