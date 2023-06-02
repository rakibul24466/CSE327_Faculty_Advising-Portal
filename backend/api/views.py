from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from api.serializer import CommentSerializer,EmailSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ScheduleNSU import class_schedule_tuple


def home(request):
    return render(request,"home.html")

from datetime import datetime

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')
from rest_framework.renderers import JSONRenderer

def login_page_api(request):
    # if request.method == 'POST':
    serializer = CommentSerializer(comment)
    serializer.data
    print(serializer.data)
    json = JSONRenderer().render(serializer.data)
    print(json)
    return render(request,"login.html",{"data":serializer.data})
    return Res
    # return render(request,'home.html')
    
    
class Email:
    def __init__(self, email, created=None):
        self.mail = email
        self.created = created or datetime.now()


import pandas as pd
import os
@api_view(['GET', 'POST'])
def login_page(request):
        a = pd.read_csv("static/class_slots.csv")
        print(type(a))
        # for i in a:
        #     print(i)
        # print(class_schedule_tuple)
        # print(request.GET["email"])
        # mail  = Email(email="Saeem@gmail.com")
        # mail = EmailSerializer(mail)
        # print(mail.data)
        # return Response(mail.data)
        return Response("mail")
  

    
