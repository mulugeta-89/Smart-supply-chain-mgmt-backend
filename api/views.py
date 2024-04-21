from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import CustomUser, BuyerProfile, Product, Order, Message
from django.contrib.auth import authenticate
from .serializers import CustomUserSerializer, BuyerProfileSerializer, SellerProfileSerializer, DriverProfileSerializer, ProductSerializer, OrderSerializer, MessageSerializer

class BuyerCreateView(APIView):
    def post(self, request):
        user_serializer = CustomUserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_instance = user_serializer.save()
            
            # Create a buyer profile associated with the new user
            buyer_data = {'user': user_instance.id}
            buyer_serializer = BuyerProfileSerializer(data=buyer_data)
            if buyer_serializer.is_valid():
                buyer_serializer.save()
                return Response({'message': 'Buyer created successfully.'}, status=status.HTTP_201_CREATED)
            else:
                # Rollback user creation if buyer profile creation fails
                user_instance.delete()
                return Response(buyer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if username is None and password is None:
            return Response({"error": "Please provide both username and password"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"login": "successful", "token": token.key}, status=status.HTTP_201_CREATED)
class SellerCreateView(APIView):
    def post(self, request):
        user_serializer = CustomUserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_instance = user_serializer.save()
            
            # Create a seller profile associated with the new user
            seller_data = {'user': user_instance.id, "tax_number": request.data.get("tax_number")}
            seller_serializer = SellerProfileSerializer(data=seller_data)
            if seller_serializer.is_valid():
                seller_serializer.save()
                return Response({'message': 'Seller created successfully.'}, status=status.HTTP_201_CREATED)
            else:
                # Rollback user creation if seller profile creation fails
                user_instance.delete()
                return Response(seller_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DriverCreateView(APIView):
    def post(self, request):
        user_serializer = CustomUserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_instance = user_serializer.save()
            
            # Create a driver profile associated with the new user
            driver_data = {'user': user_instance.id, 'license_number': request.data.get('license_number'), "car_model": request.data.get("car_model")}
            driver_serializer = DriverProfileSerializer(data=driver_data)
            if driver_serializer.is_valid():
                driver_serializer.save()
                return Response({'message': 'Driver created successfully.'}, status=status.HTTP_201_CREATED)
            else:
                # Rollback user creation if driver profile creation fails
                user_instance.delete()
                return Response(driver_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user.sellerprofile)
    
    # GET method to list all products
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class OrderCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user.buyerprofile)
class SendMessageAPIView(APIView):
    def post(self, request):
        request.data['sender'] = request.user
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            # Assuming sender is the current authenticated user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InboxAPIView(APIView):
    def get(self, request):
        # Get all messages where the current user is the recipient
        messages = Message.objects.filter(recipient=request.user)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)