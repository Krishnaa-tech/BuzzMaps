"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('',views.HomePage,name='home'),
    
    path('create_user/',views.create_user,name='create_user'),
    path('logout/',views.LogoutPage,name='logout'),
    path('create_department/',views.create_department,name='create_department'),
    path('create_course/',views.create_course,name='create_course'),
    path('create_batch/',views.create_batch,name='create_batch'),
    path('create_class/',views.create_class,name='create_class'),
    path('create_section/',views.create_section,name='create_section'),
    path('create_user/',views.create_user,name='create_user'),
    # path('userdetails/<int:id>/',views.UserDetails,name='userdetails'),
    # path('edituser/<int:id>/',views.EditUser,name='edituser'),
    # path('deleteuser/<int:id>/',views.DeleteUser,name='deleteuser')
]
