
from django.urls import path,include
from api import views
urlpatterns = [
    path("home",views.home,name="home"),
    path("login",views.LoginView.as_view(),name="login_page"),
    path("login_api",views.login_page_api,name="login_page"),
    path('accounts', include('django.contrib.auth.urls')),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.RegistrationAPIView.as_view(), name='register'),
    path('faculty_register', views.FacultyRegistrationAPIView.as_view(), name='faculty_register'),
    path('form', views.Form, name='form'),
]