from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
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

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
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


request. user.is_superuser:

UserDepartments(department=request.POST['nDepartment'], batch=request.POST[ 'nBatch'], course=request.POST['nCourse'], classnane=request..POST['nClass'],
createdon=datetine. now(tz=get_current_tinezone()), createdby=request.user)

dept save()

uploaded_file = request.FILES["document"]

filepath = "uploads/" + datetime.now()._str_() + '_' + uploaded file.name
fs = FileSystenStorage()

fs.save(filepath, uploaded file)

file data = open(MEDIA ROOT. _str_() + "/" + str(filepath), 'r')
for line in file data.readlines()
	if not 'REGISTER_NO' in line:
		fields = line.split(",")
		# print (fields)
		Password = ""
		for 1 in range(10):
			Password += 0TPgigits[math. floor (random. randon() * 10)]
		try:

			#creating user

			# auth user model columns

			# password, username, First name, last name, email

			user = User (usernane=fields[3]..strip(), first 					name=fields[1].strip(), lastname=rields[2].strip(),email 				Fields[3].strip(), password=make_password(Password), is_staff=False, 			is active=True)

			user. save()

			# user details table acts as a extension for django user model
			# user_id (FK), reg emp_id, gender, department, batch, course, 				phoneno, role,class, password
			userDetails = UserDetails(user_id=user, reg_emp_id=fields[6].strip(), 			gender=rields[5].strip(), password=Password, phone 					no=fields[4].strip(),role=request.POST['nuserType'].strip()
			userDetails. save()
		except:
			messages. error (request,
				“Error: The Users are alredy created / The email id is alredy 			in use

messages. success(request, 'File processed successfully’)
return redirect(’create_user-admin')
