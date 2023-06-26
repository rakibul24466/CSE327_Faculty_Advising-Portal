
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.authtoken.models  import Token
from rest_framework  import status
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import serializers
from .models import Faculty, Course, Section, Classroom, ClassSlot



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
        


class FacultySerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.faculty = Faculty.objects.create(
            name='John Doe',
            initial='JD',
            designation='Professor',
            email='johndoe@example.com',
            ext=1234,
            room=101,
            mobile='1234567890',
            total_credit=10.5,
            user=self.user
        )
        self.serializer = FacultySerializer(instance=self.faculty)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(
            data.keys(),
            ['id', 'name', 'initial', 'designation', 'email', 'ext', 'room', 'mobile', 'total_credit', 'user']
        )
        self.assertEqual(data['name'], 'John Doe')
        self.assertEqual(data['email'], 'johndoe@example.com')
        self.assertEqual(data['user'], self.user.id)


class CourseSerializerTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Mathematics',
            code='MATH101',
            credit=3.0,
            type='Theory',
            number_of_section=2
        )
        self.serializer = CourseSerializer(instance=self.course)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(
            data.keys(),
            ['id', 'name', 'code', 'credit', 'type', 'number_of_section']
        )
        self.assertEqual(data['name'], 'Mathematics')
        self.assertEqual(data['code'], 'MATH101')
        self.assertEqual(data['credit'], 3.0)


class SectionSerializerTest(TestCase):
    def setUp(self):
        self.faculty = Faculty.objects.create(name='John Doe', initial='JD')
        self.course = Course.objects.create(name='Mathematics', code='MATH101')
        self.section = Section.objects.create(
            no=1,
            course=self.course,
            faculty=self.faculty
        )
        self.serializer = SectionSerializer(instance=self.section)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(
            data.keys(),
            ['id', 'no', 'course', 'faculty', 'time_slot', 'classroom']
        )
        self.assertEqual(data['no'], 1)
        self.assertEqual(data['course'], self.course.id)
        self.assertEqual(data['faculty'], self.faculty.id)


class ClassroomSerializerTest(TestCase):
    def setUp(self):
        self.classroom = Classroom.objects.create(
            roomNo='101',
            seat=50,
            details='Classroom with projectors'
        )
        self.serializer = ClassroomSerializer(instance=self.classroom)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(
            data.keys(),
            ['roomNo', 'seat', 'details']
        )
        self.assertEqual(data['roomNo'], '101')
        self.assertEqual(data['seat'], 50)


class ClassSlotSerializerTest(TestCase):
    def setUp(self):
        self.classroom = Classroom.objects.create(roomNo='101', seat=50, details='Classroom with projectors')
        self.class_slot = ClassSlot.objects.create(slot=1, available=True, classroom=self.classroom)
        self.serializer = ClassSlotSerializer(instance=self.class_slot)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(
            data.keys(),
            ['id', 'name', 'slot', 'available', 'classroom']
        )
        self.assertEqual(data['slot'], 1)
        self.assertEqual(data['available'], True)
        self.assertEqual(data['classroom'], self.classroom.roomNo)


class ModelsTestCase(TestCase):
    def test_models(self):
        # Test the creation of model instances
        user = User.objects.create(username='testuser')
        faculty = Faculty.objects.create(
            name='John Doe',
            initial='JD',
            designation='Professor',
            email='johndoe@example.com',
            ext=1234,
            room=101,
            mobile='1234567890',
            total_credit=10.5,
            user=user
        )
        course = Course.objects.create(
            name='Mathematics',
            code='MATH101',
            credit=3.0,
            type='Theory',
            number_of_section=2
        )
        section = Section.objects.create(
            no=1,
            course=course,
            faculty=faculty
        )
        classroom = Classroom.objects.create(
            roomNo='101',
            seat=50,
            details='Classroom with projectors'
        )
        class_slot = ClassSlot.objects.create(slot=1, available=True, classroom=classroom)

        # Test the string representation of the models
        self.assertEqual(str(faculty), 'JD')
        self.assertEqual(str(course), 'MATH101 (Theory) ')
        self.assertEqual(str(section), 'Mathematics 1')
        self.assertEqual(str(classroom), '101')
        self.assertEqual(str(class_slot), '101 1 1')

        # Test the model methods and attributes
        self.assertEqual(faculty.user.username, 'testuser')
        self.assertEqual(course.number_of_section, 2)
        self.assertEqual(classroom.seat, 50)
        self.assertEqual(class_slot.name, 'Monday')
        self.assertEqual(class_slot.classroom, classroom)

        # Test model relationships
        self.assertEqual(section.course, course)
        self.assertEqual(section.faculty, faculty)
        self.assertEqual(section.time_slot, class_slot)
        self.assertEqual(section.classroom, classroom)


# Run the tests
