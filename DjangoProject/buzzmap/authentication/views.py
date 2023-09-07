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

def admin_users(request):
    return render(request,'main/admin_users.html')
