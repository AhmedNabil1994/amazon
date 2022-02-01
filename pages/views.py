from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Myusers
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout


def parentPage(request):
    return render(request, 'parentPage.html')

def home(request):
    return render(request,'home.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    if (request.method == 'GET'):
        return render(request, 'login.html')
    else:

        username = request.POST['username']
        password = request.POST['password']
        myUser =Myusers.objects.all().filter(userName=username,userPassword=password)
        # authuser=authenticate(username=username,usernassword=password)
        for user in myUser:
            if user.userName==username and user.userPassword==password:
                # use context 
                # user=user.userName
                # return render(request, 'home.html',{'name':user})

                # use session
                request.session['username']= username
                # authlogin(request,authuser)
                return redirect("home")
            else:
                return render(request, "login.html")
        
        # if (len(myUser)>0)  and authuser is not None  :
        #     # use context 
        #     # user=user.userName
        #     # return render(request, 'home.html',{'name':user})

        #     # use session
        #     request.session['username']= username
        #     authlogin(request,authuser)
        #     return redirect("home")
        # else:
        #     return render(request, "login.html")


def register(request):
    if (request.method == 'GET'):
        return render(request, 'register.html')
    else:
        #  Myusers.objects.create(username = request.POST['username'], email = request.POST['email'],password =request.POST['password'])

         username = request.POST['username']
         email = request.POST['email']
         password =request.POST['password']
         Myusers.objects.create(userName=username, userEmail=email, userPassword=password)
         if request.POST.get('check',True):
            #  admin user 
          User.objects.create_user(username=username,password=password,is_staff=True)
         else:
          User.objects.create_user(username=username, password=password, is_staff=False)
         return redirect (login)
        #  return render(request, 'register.html')

def insert(request):
    if (request.method == 'GET'):
        return render(request, 'insert.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        password =request.POST['password']
        Myusers.objects.create(userName=username, userEmail=email, userPassword=password)
    return render(request, 'insert.html')

def delete(request):
    if (request.method == 'GET'):
        return render(request, 'delete.html')
    else:
        context = {}
        id = request.POST['id']

        Myusers.objects.filter(userId=id).delete()
        users = Myusers.objects.all()
        context['users'] = users
        return render(request, 'delete.html',context)

def selectAll(request):
    context = {}
    users = Myusers.objects.all()
    context['users'] = users
    return render(request, 'select_all.html',context)

def selectWhere(request):
    context={}
    if (request.method == 'GET'):
        return render(request, 'select_where.html')
    else:
         username = request.POST['username']
         users =Myusers.objects.filter(userName=username)
         context['users'] = users
         return render(request, 'select_where.html',context)
def update(request):
    if (request.method == 'GET'):
        return render(request, 'update.html')
    else:
        id = request.POST['id']
        username = request.POST['username']
        email = request.POST['email']
        password =request.POST['password']
        Myusers.objects.filter(userId=id).update(userName=username,userEmail=email,userPassword=password)
    return render(request, 'update.html')

def mylogout(request):
    pass