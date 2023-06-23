from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ScheduleNSU import class_schedule_tuple
from rest_framework import authentication, permissions

def home(request):
    return render(request,"home.html")

from datetime import datetime

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')
from rest_framework.renderers import JSONRenderer

def login_page_api(request):
    # if request.method == 'POST':
    # serializer = CommentSerializer(comment)
    # serializer.data
    # print(serializer.data)
    # json = JSONRenderer().render(serializer.data)
    # print(json)
    # return render(request,"login.html",{"data":serializer.data})
    return Res
    # return render(request,'home.html')
    
    
class Email:
    def __init__(self, email, created=None):
        self.mail = email
        self.created = created or datetime.now()

from django.contrib.auth import authenticate, login


from . import serializers
from rest_framework import status
# @api_view(['GET', 'POST'])
# def login_page(request):
#         if request.method == 'POST':
#             serializer = serializers.AuthUserSerializer(data=request.data)
#             if serializer.is_valid():
#                 user = authenticate(request, username=serializer.validated_data['email'], password=serializer.validated_data['password'])
#                 if user is not None:
#                     login(request,user)
#                     return Response(serializer.data,status=status.HTTP_201_CREATED)
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         return Response("Not a post request")
  

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
# class login_page(APIView):
#     authentication_classes = [TokenAuthentication, SessionAuthentication]
#     permission_classes = [AllowAny]

#     def post(self, request):
#         # Perform authentication logic here
#         # Retrieve username and password from request data
#         username = request.data.get('username')
#         password = request.data.get('password')

#         # Perform authentication, e.g., by using Django's built-in authentication
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             # Successful authentication
#             # Generate or retrieve the authentication token for the user
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         else:
#             # Invalid credentials
#             return Response({'error': 'Invalid credentials'}, status=400)


# class LogoutAPIView(APIView):
#     authentication_classes = [TokenAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         # Get the user's authentication token
#         token = request.auth
#         print(token)
#         print(request)
#         if token is not None:
#             # Delete the authentication token
#             token.delete()
#             print('Token Deleted Successfully')
#             print('Token Deleted Successfully')

#         return Response({'message': 'Logout successful'})

from rest_framework import authentication
class LoginView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes=[AllowAny]
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        print(request.data)   
        user = authenticate(username=username, password=password)
        if user is not None:
            token = Token.objects.create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid username or password'})
    
class LogoutView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        token = request.auth

        try:
            Token.objects.get(key=token).delete()
            return Response({'success': True})
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'})



from . import serializers

class RegistrationAPIView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = serializers.RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(status.HTTP_201_CREATED,{'message': str(user)+'Registration successful'})
        return Response(serializer.errors, status=400)
    


class FacultyRegistrationAPIView(APIView):
    permission_classes=[AllowAny]
    
    def post(self, request):
        serializer = serializers.FacultyRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            faculty = serializer.save()
            return Response({'message': str(faculty)+'Registration successful'})
        return Response(serializer.errors, status=400)
    

def Form(request):
    if request.method == "GET":
        return render(request,'form.html')