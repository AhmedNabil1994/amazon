from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout
from .forms import *
from django.views import View
from django.views.generic import ListView 


def parentPage(request):
    return render(request, 'parentPage.html')

def home(request):
    # try:
        if request.session["username"] is not None:
            return render(request,'home.html')
    # except:
        else:
            return redirect(login)



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
        authuser=authenticate(username=username,password=password)
        # for user in myUser:
        #     if user.userName==username and user.userPassword==password:
        #         # use context 
        #         # user=user.userName
        #         # return render(request, 'home.html',{'name':user})

        #         # use session
        #         request.session['username']= username
        #         # authlogin(request,authuser)
        #         return redirect("home")
        #     else:
        #         return render(request, "login.html")
        
        if (len(myUser)>0):
            # use context 
            # user=user.userName
            # return render(request, 'home.html',{'name':user})
            if (authuser is not None):
                authlogin(request,authuser)
            # use session
            request.session['username']= username
            return redirect("home")
        else:
            context={}
            context["msg"]="invalid username or password"
            return render(request, "login.html",context)

# class based view
class Register(View):
    def get(self,request):
        return render(request, 'register.html')
    
    def post(self,request):
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

# old definition fn view

# def register(request):
#     if (request.method == 'GET'):
#         return render(request, 'register.html')
#     else:

#          username = request.POST['username']
#          email = request.POST['email']
#          password =request.POST['password']
#          Myusers.objects.create(userName=username, userEmail=email, userPassword=password)
#          if request.POST.get('check',True):
#             #  admin user 
#           User.objects.create_user(username=username,password=password,is_staff=True)
#          else:
#           User.objects.create_user(username=username, password=password, is_staff=False)
#          return redirect (login)

    # lab 3 insert
# def insert(request):
#     if (request.method == 'GET'):
#         return render(request, 'insert.html')
#     else:
#         username = request.POST['username']
#         email = request.POST['email']
#         password =request.POST['password']
#         Myusers.objects.create(userName=username, userEmail=email, userPassword=password)
#     return render(request, 'insert.html')

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
    request.session.clear()
    return redirect(login)

# lab 4 insert using forms
def insert(request):
    context={}
    form=InsertUsers()
    if (request.method == 'GET'):
        context['form']=form 
        return render(request, 'insert.html',context)
    else:
        username = request.POST['userName']
        email = request.POST['userEmail']
        password =request.POST['userPassword']
        Myusers.objects.create(userName=username, userEmail=email, userPassword=password)
    return render(request, 'insert.html',context)

    # lab 4 insert using forms.modelform
def insertUsingModel(request):
    context={}
    form=InsertUsersModel()
    if (request.method == 'GET'):
        context['form']=form 
        return render(request, 'insertUsingModel.html',context)
    else:
        context['form']=form
        formAfterInsert=InsertUsersModel(request.POST)
        formAfterInsert.save()
        return render(request, 'insertUsingModel.html',context)

class Myusers_list(ListView):
    model=Myusers


class Insert_trainee(View):
    context={}
    form=InsertTrainee()
    context['form']=form 
    def get(self,request):
        return render(request,"insert_trainee.html",self.context)
    def post(self,request):
        name=request.POST["name"]
        track_id=request.POST["track_id"]
        trackObject=Track.objects.get(id=track_id)
        Trainee.objects.create(name=name,track=trackObject)
        return render(request,"insert_trainee.html",self.context)

