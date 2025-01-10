from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
import firebase_admin
from firebase_admin import auth

class FirebaseAuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="password123")
    
    def test_authentication(self):
        # Simulate getting Firebase token
        token = auth.create_custom_token(self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get('/api/restaurants/')
        self.assertEqual(response.status_code, 200)
