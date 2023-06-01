
from django.urls import path,include
from api import views
urlpatterns = [
    path("home",views.home,name="home"),
    path("login",views.login_page,name="login_page"),
    path("login_api",views.login_page_api,name="login_page"),
    path('accounts/', include('django.contrib.auth.urls')),
]