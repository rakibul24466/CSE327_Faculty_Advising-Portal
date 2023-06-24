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
            
    def delete(self, request):
        try:
            code = request.data['code']
            if request.data['section'] is not None:
                section = int(request.data['section'])
                course = models.Section.objects.get(course=code,no=section)
                course.delete()
                return Response({'message': str(course )+' course successfully deleted.'})
            course = models.Course.objects.get(code=code)
            course.delete()
            return Response({'message': str(course )+' course successfully deleted.'})
        except models.Section.DoesNotExist: 
            return Response({"message":str(course)+" - " + "course could not be found"})



class GetAllCourseAPIView(APIView):
    
    authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes=[AllowAny]
    
    
    #get all courses using GET request
    def get(self, request):
        try:
            course = models.Course.objects.all()
            serializer = serializers.CourseSerializer(course,many=True)
            return Response( serializer.data)
        except models.Course.DoesNotExist:
            return Response({'message': 'course list is empty or Cannot connect the database.'})
      
    #get course by course code using POST request   
    def post(self, request):
        code = request.data['code']
        try:
            course = models.Course.objects.get(code=code)
            serializer = serializers.CourseSerializer(course)
            return Response( serializer.data)
        except models.Course.DoesNotExist:
            return Response({'message': str(code )+' has not been offered this semester'})
        
        
class GetAllFacultyAPIView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes=[AllowAny]
    
    
    #get all faculties using GET request
    def get(self, request):
        try:
            faculty = models.Faculty.objects.all()
            serializer = serializers.FacultySerializer(faculty,many=True)
            return Response( serializer.data)
        except models.Faculty.DoesNotExist:
            return Response({'message': 'Faculty list is empty or Cannot connect the database.'})
      
    #get faculty by initial code using POST request   
    def post(self, request):
        initial = request.data['initial']
        try:
            faculty = models.Faculty.objects.get(initial=initial)
            serializer = serializers.FacultySerializer(faculty)
            return Response( serializer.data)
        except models.Faculty.DoesNotExist:
            return Response({'message': str(initial )+' has not been taking course this semester'})
        
        
class GetAllClassroomAPIView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes=[AllowAny]
    
    
    #get all classroom using GET request
    def get(self, request):
        try:
            classroom = models.Classroom.objects.all()
            serializer = serializers.ClassroomSerializer(classroom,many=True)
            return Response( serializer.data)
        except models.Classroom.DoesNotExist:
            return Response({'message': 'Faculty list is empty or Cannot connect the database.'})
      
    ##get classroom by classroom no and building intial using POST request   
    def post(self, request):
        building= request.data['building']
        roomNo= request.data['roomNo']
        try:
            classroom = models.Classroom.objects.get(building=building,roomNo=roomNo)
            serializer = serializers.ClassroomSerializer(classroom )
            return Response( serializer.data)
        except models.Classroom.DoesNotExist:
            return Response({'message': str(classroom )+' has not been taking course this semester'})
    

class CreateClassroomAPIView(APIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes=[AllowAny]
    
    #Creating classroom
        #using classroom number
        #using the buildin and floor details at a whole
    def post(self, request):
        building = request.data['building_name']
        if request.data['roomNo'] is not None :
            roomNo = request.data['roomNo']
            total_seat =  int(request.data["total_seat"])
            details =  request.data["detail"]
            classroom = models.Classroom.objects.create(building=building,roomNo=roomNo,seat=total_seat,details=details)
            return Response({"message":str(classroom )+" has been created with all the slots"})
        else:
            total_floor = int(request.data['total_floor'])
            per_floor = int(request.data['perfloor'])
            total_seat =  int(request.data["total_seat"])
            details =  request.data["detail"]
            for i in range(total_floor):
                for j in range(per_floor):
                    classroom = models.Classroom.objects.create(building=building,roomNo=i*100+j,seat=total_seat,details=details)
            return Response({"message":str(classroom )+" has been created with all the slots"})
    
    
    def delete(self, request):
        try:
            building = request.data['building_name']
            roomNo = request.data['roomNo']
            classroom = models.Classroom.objects.get(building=building,roomNo=roomNo)
            classroom.delete()
            return Response({"message":building+" - " + roomNo+ " has been deleted with all the slots"})
        except models.Classroom.DoesNotExist: 
            return Response({"message":building+" - " + roomNo+" could not be found"})

              
              