from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ScheduleNSU import class_schedule_tuple
from rest_framework import authentication, permissions
from datetime import datetime
from django.contrib.auth import authenticate, login
from . import serializers
from . import models

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt


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


class RegistrationAPIView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = serializers.RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(status.HTTP_201_CREATED,{'message': str(user)+'Registration successful'})
        return Response(serializer.errors, status=400)
    


class FacultyRegistrationAPIView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes=[AllowAny]
    
    def post(self, request):
        serializer = serializers.FacultyRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            faculty = serializer.save()
            return Response({'message': str(faculty)+'Registration successful'})
        return Response(serializer.errors, status=400)
    

##Course Create 
class CourseCreateAPIView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes=[AllowAny]
    
    def post(self, request):
        name = request.data['name']
        code = request.data['code']
        try:
            course = models.Course.objects.get(code=code)
            return Response({'message': str(course )+' already exist with  {} sections.'.format(course.number_of_section)})
        
        except models.Course.DoesNotExist:
            credit = request.data['credit']
            course_type = request.data['type']
            section_to_be_open = int(request.data['no_of_sections'])
            course = models.Course(name=name,code=code,credit=credit,type=course_type,number_of_section = section_to_be_open)
            course.save()
            return Response({'message': str(course )+' created successfully with total {} sections.'.format(section_to_be_open)})
            
        

##Faculty Course Registration
class CourseCreateAPIView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes=[AllowAny]
    
    def post(self, request):
        #check whether course if offered
        code = request.data['code']
        
        ##classroom verify and create 
        building = request.data['building']
        room_no = request.data['room_no']
        number_of_seat = request.data['number_of_seat']
        details = request.data['details']
        classroom = models.Classroom(building=building,roomNo=room_no,seat=number_of_seat,details=details)
        
        try:
            course = models.Course.objects.get(code=code)
            return Response({'message': str(course )+' already exist with  {} sections.'.format(course.number_of_section)})
        
        except models.Course.DoesNotExist:
            credit = request.data['credit']
            course_type = request.data['type']
            section_to_be_open = int(request.data['no_of_sections'])
            course = models.Course(name=name,code=code,credit=credit,type=course_type,number_of_section = section_to_be_open)
            course.save()
            return Response({'message': str(course )+' created successfully with total {} sections.'.format(section_to_be_open)})
            
#get all courses using GET request
#get course by course code using POST request
class GetAllCourseAPIView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes=[AllowAny]
    
    def get(self, request):
        try:
            course = models.Course.objects.all()
            serializer = serializers.CourseSerializer(course,many=True)
            return Response( serializer.data)
        except models.Course.DoesNotExist:
            return Response({'message': 'course list is empty or Cannot connect the database.'})
        
    def post(self, request):
        code = request.data['code']
        try:
            course = models.Course.objects.get(code=code)
            serializer = serializers.CourseSerializer(course)
            return Response( serializer.data)
        except models.Course.DoesNotExist:
            return Response({'message': str(code )+' has not been offered this semester'})