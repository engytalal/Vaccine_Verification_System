"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include , re_path
from project.settings import SECRET_KEY
from webapp import views
from webapp.views import p1,p2 ,p3,p4,p5,p6,add,showdata
from rest_framework import routers
from datetime import timedelta
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
r=routers.DefaultRouter()
r.register('',views.userView)

r1=routers.DefaultRouter()
r1.register('',views.employeeView)

r2=routers.DefaultRouter()
r2.register('',views.adminView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',p1,name='index'),
    path('login/',p2,name='login'),
    path('logout/',p3,name='logout'),
    path('verification/',p4, name='verification'),
    path('home/',p5,name='home'),
    path('addperson/',p6,name='addperson'),
    path('add/',add,name='add'),
    path('show/',showdata,name='showdata'),
    path('users/',include(r.urls)),
    path('employees/',include(r1.urls)),
    path('admins/',include(r2.urls)),
    path('api-auth/', include ("rest_framework.urls")),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    re_path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    re_path('auth/', include('djoser.urls.jwt')),
]

