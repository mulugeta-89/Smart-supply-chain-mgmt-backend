from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Buyer
from .serializers import BuyerSerializer, SellerSerializer, DriverSerializer

class BuyerCreateRetrieveUpdateDestroyViewTest(APITestCase):
    def setUp(self):
        self.buyer = Buyer.objects.create(username="testuser", password="testpassword", full_name="Test User", phone_number="1234567890", address="123 Test St", payment_method="Credit Card")

    def test_create_buyer(self):
        sample = {
            "username": "testuser",
            "password": "testpassword",
            "full_name": "Test User",
            "phone_number": "1234567890",
            "address": "123 Test St",
            "payment_method": "Credit Card"
        }
        url = reverse("buyer-create-view")
        response = self.client.post(url, sample)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Buyer.objects.count(), 2)
    def test_retrieve_buyer(self):
        buyer = Buyer.objects.create(username="testuser", password="testpassword", full_name="Test User", phone_number="1234567890", address="123 Test St", payment_method="Credit Card")
        url = reverse("buyer-update-destroy-view", kwargs={"pk": buyer.pk})
        response = self.client.get(url)
        serializer = BuyerSerializer(instance=buyer)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_buyer(self):
        url = reverse("buyer-update-destroy-view", args=[self.buyer.userId])
        updated_data = {
            "username": "updateduser",
            "full_name": "Updated User",
            "password": "newpassword",  # Include required fields
            "phone_number": "1234567890",
            "address": "123 Test St",
            "payment_method": "Credit Card",
        }
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.buyer.refresh_from_db()
        self.assertEqual(self.buyer.username, "updateduser")
        self.assertEqual(self.buyer.full_name, "Updated User")

    def test_delete_buyer(self):
        url = reverse("buyer-update-destroy-view", args=[self.buyer.userId])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Buyer.objects.count(), 0)
