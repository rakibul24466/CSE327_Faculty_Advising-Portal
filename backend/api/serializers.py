from rest_framework import serializers
from django.contrib.auth.models import User
from . import models



class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']
        

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faculty
        fields = '__all__'


class FacultyRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faculty
        fields = ["name","designation"]

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Classroom
        fields = '__all__'
        
class ClassroomRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Classroom
        fields = ["roomNo","seat"]


class ClassSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClassSlot
        fields = '__all__'
        
class ClassSlotRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClassSlot
        fields = ['name']

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = '__all__'
        
class CourseRoutineSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = ['name','code','credit','type']

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
class FacultyRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    
    class Meta:
        model = models.Faculty
        fields = ['username','password','email', 'name', 'initial','room','mobile']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        initial = validated_data['initial']
        email = validated_data['email']
        name = validated_data['name']
        room  = validated_data['room']
        mobile = validated_data['mobile']
        user.set_password(validated_data['password'])
        faculty = models.Faculty.objects.create(user=user,initial=initial,email=email,name=name,room=room,mobile=mobile)
        user.save()
        faculty.save()
        return faculty
    
class SectionSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer( read_only=True)
    course = CourseSerializer( read_only=True)
    time_slot = ClassSlotSerializer(read_only=True)
    classroom = ClassroomSerializer(read_only=True)
    
    
    class Meta:
        model = models.Section
        fields = '__all__'


class SectionNewSerializer(serializers.ModelSerializer):
    course = CourseSerializer( read_only=True)
    classroom = ClassroomSerializer(read_only=True)
    
    
    class Meta:
        model = models.Section
        fields = '__all__'

class SectionRoutineSerializer(serializers.ModelSerializer):
    faculty = FacultyRoutineSerializer(read_only=True)
    course = CourseRoutineSerializer( read_only=True)
    time_slot = ClassSlotRoutineSerializer(read_only=True)
    classroom = ClassroomRoutineSerializer(read_only=True)
    
    class Meta:
        model = models.Section
        fields = '__all__'

