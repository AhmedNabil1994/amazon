from django.shortcuts import render
from django.http import HttpResponse
from .models import Myusers
def parentPage(request):
    return render(request, 'parentPage.html')

def home(request):
    return render(request,'home.html',{'name':'Nabeel'})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    if (request.method == 'GET'):
        return render(request, 'login.html')
    else:

        email = request.POST['email']
        password = request.POST['password']
        myUser=Myusers.objects.all()
        for user in myUser:

            if user.userEmail==email and user.userPassword==password:
                user=user.userName
                return render(request, 'home.html',{'name':user})
            else:
                return render(request, "login")

def register(request):
    if (request.method == 'GET'):
        return render(request, 'register.html')
    else:
         username = request.POST['username']
         email = request.POST['email']
         password =request.POST['password']
         Myusers.objects.create(userName=username, userEmail=email, userPassword=password)
         return render(request, 'register.html')
