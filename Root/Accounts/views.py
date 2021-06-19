from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
# Create your views here.

# user = auth.authentication(username = username,password = password)
# if user is not None:
#   auth.login(request,user)
#   return redirect("/")

def login(request):
    if(request.method == 'POST'):
        requestType = request.POST['requestPage']
        if(requestType == '0'):     # i.e login request
            username = request.POST['userName']
            password = request.POST['password']
            user = authenticate(username = username,password = password)
            if user is not None:
                print("Successfully authenticated")
                auth.login(request,user)
                return redirect('/')
            else:
                print("Invalid credentials")
                return redirect('login')
        else:   #i.e register request
            first_name = request.POST['firstName']
            last_name = request.POST['lastName']
            email = request.POST['email']
            username = request.POST['userName']
            password = request.POST['password']
            if User.objects.filter(username = username).exists():
                print("user already registered")
                return redirect('login')
            if User.objects.filter(email = email).exists():
                print("email already registered")
                return redirect('login')
            user  = User.objects.create_user(username = username,first_name = first_name,last_name = last_name,email = email,password = password)
            user.save()
            return redirect('login')
    else:
        return render(request,'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')