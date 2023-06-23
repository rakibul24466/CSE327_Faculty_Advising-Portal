
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.authtoken.models  import Token
from rest_framework  import status



class LoginLogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example",password="newpassword@123")
        
    def test_login(self):
        data = {
            "username" : "example",
            # "password" : "newpassword@123"
            "password" : "newpassword"
        }
        response = self.client.post(reverse('login'),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def logout_test(self):
        self.token = Token.objects.get(user__username="example")
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)