from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages,auth


from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
#from django.contrib.auth.models import User




def register1(request):
    print("my request", request.POST)
    
    if request.method == 'POST':
        print("request is post")
        
        User = get_user_model()
        form = UserCreationForm(request.POST)
        print("this my form, " ,form )
        if form.is_valid():
            user = form.save(commit=False)
            user_type = request.POST.get('user_type')
            if user_type == 'author':
                author_id = request.POST.get('author_id')
                # validate author ID here
                user.author_id = author_id
            elif user_type == 'publisher':
                license = request.POST.get('license')
                # validate publishing house license here
                user.license = license
            user.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'users/registration.html', {'form': form})


from .forms import SignUpForm
def register(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		
	else:
		form = SignUpForm()

	context = {'form': form}
	return render(request, 'users/registration.html', context)

# def register(request):
#     if request.method == 'POST':
#         #Get form Values 
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         #check if password match
#         if password == confirm_password:
#             #check username
#             if User.objects.filter(username=username).exists():
#                 messages.error(request,"That username is taken")
#                 return redirect('register')
#             else:
#                 if User.objects.filter(email=email).exists():
#                     messages.error(request,"That email is being used.")
#                     return redirect('register')
#                 else:
#                     user = User.objects.create_user(username=username,email=email,password=password)
#                     user.save()
#                     messages.success(request,'You are now registered and can login in')
#                     return redirect('login')
#         else:
#             messages.error(request, "Password do not match.")
#             return redirect('register')
#     else:
#         return render(request,'users/registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            #messages.success(request,'You are Now Logged in')
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
    else:
       return render(request,'users/login.html') 
    


def dashboard(request):
    return HttpResponse("dashboard")