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
from django.db import IntegrityError


from rest_framework import authentication
class LoginView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes=[AllowAny]
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        # print(request.data)   
        user = authenticate(username=username, password=password)
        if user is not None:
            role = ""
            token , created= Token.objects.get_or_create(user=user)
            person = None
            try:
                person = models.Faculty.objects.get(user=user)
                role = "Faculty"
                return Response({'token': token.key,'designation':person.designation,"user_email":person.email,"user_name":user.get_username(),'role':role})
            except models.Faculty.DoesNotExist:
                role = "Admin"
                return Response({'token': token.key,"user_email":user.email,"user_name":user.get_username(),'role':role})
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
    
    
    #get all courses using GET request
    def get(self, request):
        try:
            faculty = models.Faculty.objects.filter(user=request.user)[0]
            print(models.Faculty.objects.filter(user=request.user))
            if faculty:
                print("SS")
                sections = models.Section.objects.filter(faculty=faculty)
                serializer = serializers.SectionSerializer(sections,many=True)
                return Response( serializer.data)
            else:
                course = models.Course.objects.all()
                serializer = serializers.CourseSerializer(course,many=True)
                return Response( serializer.data)
        except models.Course.DoesNotExist:
            return Response({'message': 'course list is empty or Cannot connect the database.'})
    
    #get course by course code using POST request   
    def post(self, request):
        code = request.data['code']
        try:
            # sectionSerializer = None
            if "faculty_initial" in request.data:
                faculty_initial = request.data["faculty_initial"]
                faculty = models.Faculty.objects.get(initial = faculty_initial )
                course = models.Course.objects.get(code=code)
                sections = models.Section.objects.filter(course=course,faculty=faculty)
                sectionSerializer = serializers.SectionSerializer(sections,many=True)
                return Response( sectionSerializer.data)
            else:
                course = models.Course.objects.get(code=code)
                serializer = serializers.CourseSerializer(course)
                return Response( serializer.data)
        except models.Course.DoesNotExist:
            return Response({'message': str(code )+' has not been offered this semester'})
        except models.Faculty.DoesNotExist:
            return Response({'message': 'Faculty has not been taking courses this semester'})

class GetAllFacultyAPIView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    
    
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
        
class FacultyRegistrationAPIView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes=[AllowAny]
    
    def post(self, request):
        serializer = serializers.FacultyRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            faculty = serializer.save()
            return Response({'message': str(faculty)+'  Registration successful'})
        return Response(serializer.errors, status=400)
    


class CreateClassroomAPIView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    
    #Creating classroom
        #using classroom number
        #using the building and floor details at a whole
    def post(self, request):
        try:
            if 'roomNo' in request.data:
                roomNo = request.data['roomNo']
                total_seat =  int(request.data["total_seat"])
                details =  request.data["detail"]
                classroom = models.Classroom.objects.create(roomNo=roomNo,seat=total_seat,details=details)
                return Response({"message":str(classroom )+" has been created with all the slots"})
            else:
                total_floor = int(request.data['total_floor'])
                per_floor = int(request.data['per_floor'])
                total_seat =  int(request.data["total_seat"])
                details =  request.data["detail"]
                building = request.data['building_name']
                for i in range(1,total_floor+1):
                    for j in range(per_floor):
                        classroom = models.Classroom.objects.create(roomNo=building+str(i*100+j),seat=total_seat,details=details)
                return Response({"message":"All the classroom have been created with all the slots"})
        except IntegrityError as e:    
            return Response({"message":str(e)})
        
    def delete(self, request):
        try:
            roomNo = request.data['roomNo']
            classroom = models.Classroom.objects.get(roomNo=roomNo)
            classroom.delete()
            return Response({"message": roomNo+ " has been deleted with all the slots"})
        except models.Classroom.DoesNotExist: 
            return Response({"message": roomNo+" could not be found"})


class GetAllClassroomAPIView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    
    
    #get all classroom using GET request
    def get(self, request):
        try:
            #Gets all the available classroom 
            if "status" in request.data:
                status = False
                if request.data['status'] == "Available":
                    status = True
                class_slot = models.ClassSlot.objects.filter(available=status)
                classroom = class_slot.values_list('classroom', flat=True).distinct()
                classroom = models.Classroom.objects.filter(pk__in=classroom)
                serializer = serializers.ClassroomSerializer(classroom,many=True)
                return Response( serializer.data)
            #Gets all the classroom , whether it is available or not does not matter
            else:
                classroom = models.Classroom.objects.all()
                serializer = serializers.ClassroomSerializer(classroom,many=True)
                return Response( serializer.data)
        except models.Classroom.DoesNotExist:
            return Response({'message': 'Faculty list is empty or Cannot connect the database.'})
      
    ##get classroom by classroom no and building intial using POST request   
    def post(self, request):
        room_no = request.data['roomNo']
        classroom = None
        try:
            available = False
            time_slot = None
            classroom = models.Classroom.objects.get(roomNo=room_no)
            if "status" in request.data:
                if request.data['status'] == "Available":
                    available = True
                time_slot = models.ClassSlot.objects.filter(classroom=classroom,available=available)
            else:
                time_slot = models.ClassSlot.objects.filter(classroom=classroom)
            
            serializer = serializers.ClassSlotSerializer(time_slot,many=True)
            return Response( serializer.data)
        except models.Classroom.DoesNotExist:
            return Response({'message': 'Classroom not found'})



from django.utils.datastructures import MultiValueDictKeyError


from django.conf import settings
from django.core.mail import send_mail

#Course taking api
class TakeCourseAPIView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    
    def post(self,request):
        print(request.user)
        try:
            faculty = models.Faculty.objects.get( user = request.user)
            time_slot = models.ClassSlot.objects.get(pk=int(request.data['time_slot_id']))
            room_no  = request.data['room_no']
            classroom = models.Classroom.objects.get(roomNo=room_no)
            course = models.Course.objects.get(code = request.data['course_code'])
            section = models.Section.objects.get(course = course, no = int(request.data["section_no"]))
            try:
                old_faculty  = models.Faculty.objects.get(initial = section.faculty)
                if old_faculty.initial !="TBA" and old_faculty!= faculty.initial:
                    return Response({"message":"Already {} taking the section".format(old_faculty)})
                else:
                    faculty.total_credit = faculty.total_credit  + course.credit
                    if faculty.total_credit > 11:
                        return Response({"message":"Faculty can not take more than 11 credits"})
            except models.Faculty.DoesNotExist:
                pass
            if time_slot.available == False:
                return Response({"message":"Time slot is occupied"})


            if time_slot.available != section.time_slot.available:
                section.time_slot.available =True
                section.time_slot.save()
            
            section.faculty=faculty
            section.time_slot=time_slot
            section.classroom = classroom
            time_slot.available = False
            section.save()
            time_slot.save()
            faculty.save()
            print(faculty)
            section_serializer = serializers.SectionSerializer(section)
            return Response(section_serializer.data)
        except models.Faculty.DoesNotExist:
            return Response({"message":"Must be a faculty"})

        except models.ClassSlot.DoesNotExist:
            return Response({"message ":"Class Slot invalid"})
        except models.Course.DoesNotExist:
            return Response({"message":"Course not found "})
        

        except IntegrityError as e:
            return Response({"message":str(e)})

        except MultiValueDictKeyError as e:
            return Response({"message":str(e) + " Missing field"})

    def delete(self,request):
        try:
            faculty = models.Faculty.objects.get( user = request.user)
            section = models.Section.objects.get( faculty = faculty,no=request.data['section_no'])
            new_faculty = models.Faculty.objects.get(initial="TBA")
            section.faculty = new_faculty
            section.save()
            return Response({"message":"Section removed"})
        except (models.Faculty.DoesNotExist,models.Section.DoesNotExist):
            return Response({"message":"You are not taking the course"})


from django.utils.crypto import get_random_string
from django.template.loader import render_to_string
from django.utils.html import strip_tags

##Mail sending api
class SendEmail(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    def post(self,request):
        try:
            subject = 'FACS Registration'
            title = f'Hi {request.data["username"]}, thank you for registering FACS.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = request.data["email"]
            created_password = get_random_string(8)
            html_template = 'new_registration_email_format.html'
            context = {
                'username': request.data["username"],
                'password': created_password,
                'title':title 
            }
            html_content = render_to_string(html_template, context)
            
            # Generate the plain text version of the email
            plain_text_content = strip_tags(html_content)
            
            mail = send_mail( subject, message=plain_text_content, from_email = email_from, recipient_list=[recipient_list] ,html_message=html_content, fail_silently=False)
            status = "Mail sending failed."
            if mail == 1:
                status = "Mail Sent."
            return Response({"message":status,"password":created_password,"email":recipient_list})
        except IntegrityError as e:
            return Response({"message":str(e)})

        except MultiValueDictKeyError as e:
            return Response({"message":str(e) + " Missing field"})

def email_template(request):
    return render(request,"new_registration_email_format.html",{
                                                "username": "Give a username",
                                                "password":  "created_password"
                                             }
                  )