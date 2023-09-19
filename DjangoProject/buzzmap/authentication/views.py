from django.shortcuts import render

# Create your views here.
def home_login(request):
    return render(request,'auth/login.html')

def dashboard(request):
    return render(request,'main/dashboard.html')

def user_page(request):
    return render(request,'main/user_page.html')

def index(request):
    return render(request,'auth/index.html')

def support_edit(request):
    return render(request,'main/support_edit.html')

def support_view(request):
    return render(request,'main/support_view.html')

def admin_users_create(request):
    return render(request,'main/admin_users_create.html')


def admin_users_manage(request):
    return render(request,'main/admin_users_manage.html')

def user_profile(request):
    return render(request,'main/user_profile.html')

def admin_drivers_buses(request):
    return render(request,'main/admin_drivers_buses.html')

def admin_routes_landmarks(request):
    return render(request,'main/admin_routes_landmarks.html')
