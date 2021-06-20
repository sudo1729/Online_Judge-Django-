from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate

from Compiler.models import Compiler
from Compiler.serializers import CompilerSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CompilerList(APIView):


    def get(self, request, format=None):
        compiler = Compiler.objects.all()
        serializer = CompilerSerializer(compiler, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompilerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

# For login from current page

def login(request,slug):
    if(request.method == 'POST'):
        requestType = request.POST['requestPage']
        if(requestType == '0'):     # i.e login request
            username = request.POST['userName']
            password = request.POST['password']
            user = authenticate(username = username,password = password)
            if user is not None:
                print("Successfully authenticated")
                auth.login(request,user)
                return redirect('/ide/'+slug)
            else:
                print("Invalid credentials")
                return redirect('/ide/'+slug+'/login')
        else:   #i.e register request
            first_name = request.POST['firstName']
            last_name = request.POST['lastName']
            email = request.POST['email']
            username = request.POST['userName']
            password = request.POST['password']
            if User.objects.filter(username = username).exists():
                print("user already registered")
                return redirect('/ide/'+slug+'/login')
            if User.objects.filter(email = email).exists():
                print("email already registered")
                return redirect('/ide/'+slug+'/login')
            user  = User.objects.create_user(username = username,first_name = first_name,last_name = last_name,email = email,password = password)
            user.save()
            user = authenticate(username = username,password = password)
            if user is not None:
                auth.login(request,user)
                return redirect('/ide/'+slug)
            else:
                print("Invalid credentials")
                return redirect('/ide/'+slug+'/login')
    else:
        return render(request,'accounts/login.html')


def logout(request,slug):
    auth.logout(request)
    return redirect('/ide/'+slug)

# Login ends here


def check(request,slug):
    return render(request,"ide.html",{'slug':slug})