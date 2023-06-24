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

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Classroom
        fields = '__all__'


class ClassSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClassSlot
        fields = '__all__'


# class CourseTakenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.CourseTaken
#         fields = '__all__'


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
        fields = ['username','password','email', 'name', 'initial']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        initial = validated_data['initial']
        email = validated_data['email']
        name = validated_data['name']
        user.set_password(validated_data['password'])
        faculty = models.Faculty.objects.create(user=user,initial=initial,email=email,name=name)
        user.save()
        faculty.save()
        return faculty
    
class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = '__all__'