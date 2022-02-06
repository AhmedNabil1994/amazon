
from django.contrib import admin
from django.urls import path,include
from pages.views import*



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', parentPage),
    path('home', home, name = 'home'),
    path('contact', contact, name = 'contact'),
    path('about', about, name = 'about'),
    path('login', login, name = 'login'),
    path('logout', mylogout, name = 'logout'),
    path('register', Register.as_view(), name = 'register'),
    path('insert/',insert,name="insert"),
    path('selectall/',selectAll,name="selectall"),
    path('selectwhere/',selectWhere,name="selectwhere"),
    path('delete/',delete,name="delete"),
    path('update/',update,name="update"),
    path('mylogout/',mylogout,name="mylogout"),
    path('insertUsingModel/',insertUsingModel,name="insertUsingModel"),
    path('myusers_list/',Myusers_list.as_view(),name="myusers_list"),
    path('insert_trainee/',Insert_trainee.as_view(),name="insert_trainee"),
    path('myapi/',include('myapi.urls')),




]

