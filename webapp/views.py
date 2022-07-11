from django.contrib import messages
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from . import models
from .serializer import employeeserializer, userserializer, adminserializer
from rest_framework.views import APIView
from .models import employee, user 
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User, auth

class userView(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class=userserializer

class employeeView(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class=employeeserializer

class adminView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class=adminserializer

# Create your views here.
def p1(request):
    return render(request,'pages/index.html',{})

def p2(request):
    if request.method=='POST':
            email=request.POST['email']
            password=request.POST['password']
            user= auth.authenticate(email= email ,password=password)
            
            if user is not None:
                auth.login(request,user)
                return render(request,'pages/home.html',{})
            else:
                messages.info(request, 'invalid email or password')
                return render(request,'pages/login.html',{})

    else:
        return render(request,'pages/login.html',{})

def p3(request):
    return render(request,'pages/logout.html',{})

def p4(request):
    return render(request,'pages/verification.html',{})

def p5(request):
    return render(request,'pages/home.html',{})

def p6(request):
    return render(request,'pages/addperson.html',{})

def showdata(request):
    data=models.user.objects.all()
    return render(request,'pages/show.html',{'d':data})

def add(request):
    v1=request.POST['name']
    v2=request.POST['age']
    v3=request.POST['id']
    v4=request.POST['country']
    v5=request.POST['address']
    v6=request.POST['phone_num']
    b=models.user(name=v1,age=v2,Na_id=v3,country=v4,address=v5,phone_num=v6)
    b.save()
    data=models.user.objects.all()
    return render(request,'pages/show.html',{'d':data})