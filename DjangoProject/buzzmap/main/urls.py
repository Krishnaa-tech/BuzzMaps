from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import dashboard, user_page, index, support_view, support_edit, admin_users_create,admin_users_manage,admin_drivers_buses,admin_routes_landmarks,map_view_admin


urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    path('user_page/',user_page,name='user_page'),
    path('index/',index,name='index'),
    path('support_view/',support_view,name='support_view'),
    path('admin_users_create/',admin_users_create,name='admin_users_create'),
    path('admin_users_manage/',admin_users_manage,name='admin_users_manage'),
    path('support_edit/',support_edit,name='support_edit'),
    path('admin_drivers_buses/',admin_drivers_buses,name='admin_drivers_buses'),
    path('admin_routes_landmarks/',admin_routes_landmarks,name='admin_routes_landmarks'),
    path('map_view_admin/',map_view_admin,name='map_view_admin')

]
