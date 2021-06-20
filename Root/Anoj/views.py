from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def homePage(request):
    return render(request, "home.html")


def contestPage(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return redirect('login')

# def check(request,slug):
#     print(slug)
#     return HttpResponse("Success"+slug)

def ide(request):
    print(request.POST['code'])
    return HttpResponse("Success")