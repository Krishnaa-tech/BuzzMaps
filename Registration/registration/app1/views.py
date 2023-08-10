import random ,math ,datetime
from django.shortcuts import render,redirect,HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import authenticate ,login , logout
import logging
from django.shortcuts import render, redirect
from .models import UserDetails, Department, Class, Course, Batch, Section

# Create your views here.#

@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get
    return render(request,'signup.html')

def LoginPage(request):
    return render(request,'login.html')


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

    
        if pass1 != pass2:
            messages.error(request, "Your password and confirm password are not the same!!")
            return redirect('signup')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
    




def create_user(request):    
    if request.user.is_superuser:
        dept = UserDepartments(
            department=request.POST['nDepartment'],
            batch=request.POST['nBatch'],
            course=request.POST['nCourse'],
            class_name=request.POST['nClass'],
            createdon=datetime.now(tz=get_current_timezone()),createdby=request.user)
        dept.save()

        uploaded_file = request.FILES["document"]
        filepath = "uploads/" + datetime.datetime.now().__str__() + '_' + uploaded_file.name
        fs = FileSystemStorage()
        fs.save(filepath, uploaded_file)

        file_data = open(MEDIA_ROOT.__str__() + "/" + str("test.csv"),'r')

        for line in file_data.readlines():
            if not 'REGISTER_NO' in line:
                fields = line.split(",")
                Password = ""
                for i in range(10):
                    Password += OTPdigits[math.floor(random.random() * 10)] 
                try:
                    user = User(
                        username=fields[4].strip(),
                        first_name=fields[1].strip(),
                        last_name=fields[2].strip(),
                        password=make_password(Password),
                        is_staff=False,
                        is_active=True
                    )
                    user.save()

                    userDetails = UserDetails(
                        user_id=user,
                        course=fields[7].strip(),
                        batch=fields[6].strip(),
                        Class=fields[8].strip(),
                        department=fields[5].strip(),
                        phoneno=fields[3].strip(),
                        role=request.POST['nuserType'].strip()
                    )
                    userDetails.save()
                except:
                    messages.error(request, "Error: The Users are already created / The email id is already in use")

        messages.success(request, "File processed successfully")

    return redirect('create_user-admin')  # Make sure this redirect URL is correct


logger = logging.getLogger(__name__)

def create_department(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            department = Department.objects.create(name=name)
            logger.info(f"Department created: {department.name}")
            return redirect('department_list')  # Redirect to department list page
        except Exception as e:
            logger.error(f"Error creating department: {e}")
            return render(request, 'create_department.html', {'error_message': 'Error creating department'})

    return render(request, 'create_department.html')

def create_class(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department_id = request.POST.get('department_id')  # Assuming you have a form field for department_id
        try:
            department = Department.objects.get(id=department_id)
            class_instance = Class.objects.create(name=name, department=department)
            logger.info(f"Class created: {class_instance.name}")
            return redirect('class_list')  # Redirect to class list page
        except Exception as e:
            logger.error(f"Error creating class: {e}")
            return render(request, 'create_class.html', {'error_message': 'Error creating class'})

    return render(request, 'create_class.html')

def create_batch(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            batch = Batch.objects.create(name=name)
            logger.info(f"Batch created: {batch.name}")
            return redirect('batch_list')  # Redirect to batch list page
        except Exception as e:
            logger.error(f"Error creating batch: {e}")
            return render(request, 'create_batch.html', {'error_message': 'Error creating batch'})

    return render(request, 'create_batch.html')

def create_section(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        batch_id = request.POST.get('batch_id')  # Assuming you have a form field for batch_id
        try:
            batch = Batch.objects.get(id=batch_id)
            section = Section.objects.create(name=name, batch=batch)
            logger.info(f"Section created: {section.name}")
            return redirect('section_list')  # Redirect to section list page
        except Exception as e:
            logger.error(f"Error creating section: {e}")
            return render(request, 'create_section.html', {'error_message': 'Error creating section'})

    return render(request, 'create_section.html')

def create_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            course = Course.objects.create(name=name)
            logger.info(f"Course created: {course.name}")
            return redirect('Course_list')  # Redirect to department list page
        except Exception as e:
            logger.error(f"Error creating course: {e}")
            return render(request, 'create_course.html', {'error_message': 'Error creating course'})
