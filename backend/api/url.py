
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
]