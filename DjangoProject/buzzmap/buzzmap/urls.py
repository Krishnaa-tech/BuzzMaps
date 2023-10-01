"""buzzmap URL Configuration

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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from authentication.views import home_login, dashboard, user_page, index, support_view, support_edit, admin_users_create,admin_users_manage,admin_drivers_buses,admin_routes_landmarks


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_login,name='home-login'),
    path('dashboard/',dashboard,name='dashboard'),
    path('user_page/',user_page,name='user_page'),
    path('index/',index,name='index'),
    path('support_view/',support_view,name='support_view'),
    path('admin_users_create/',admin_users_create,name='admin_users_create'),
    path('admin_users_manage/',admin_users_manage,name='admin_users_manage'),
    path('support_edit/',support_edit,name='support_edit'),
    path('admin_drivers_buses/',admin_drivers_buses,name='admin_drivers_buses'),
    path('admin_routes_landmarks/',admin_routes_landmarks,name='admin_routes_landmarks')




]+ static(settings.STATIC_URL)


