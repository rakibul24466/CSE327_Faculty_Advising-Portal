
from django.urls import path,include
from api import views
urlpatterns = [
    path("login",views.LoginView.as_view(),name="login_page"),
    path('accounts', include('django.contrib.auth.urls')),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.RegistrationAPIView.as_view(), name='register'),
    path('faculty_register', views.FacultyRegistrationAPIView.as_view(), name='faculty_register'),
    path('course_create', views.CourseCreateAPIView.as_view(), name='course Create'),
    path('get_all_course', views.GetAllCourseAPIView.as_view(), name='get_all_courses'),
    path('get_all_course_faculty', views.GetAllCourseFacultyAPIView.as_view(), name='get_all_courses_faculty'),
    path('get_all_faculty', views.GetAllFacultyAPIView.as_view(), name='get_all_faculty'),
    path('get_all_classroom', views.GetAllClassroomAPIView.as_view(), name='get_all_classroom'),
    path('take_course', views.TakeCourseAPIView.as_view(), name='take_course'),
    path('create_classroom', views.CreateClassroomAPIView.as_view(), name='create_classroom'),
    path('get_faculty_timeslot', views.GetFacultyTimeslot.as_view(), name='get_faculty_timeslot'),
    path('send_mail', views.SendEmail.as_view(), name='send_mail'),
    path('mail_template', views.email_template, name='mail_template'),
]