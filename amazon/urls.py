
from django.contrib import admin
from django.urls import path
from pages.views import*


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', parentPage),
    path('home', home, name = 'home'),
    path('contact', contact, name = 'contact'),
    path('about', about, name = 'about'),
    path('login', login, name = 'login'),
    path('logout', mylogout, name = 'logout'),
    path('register', register, name = 'register'),
    path('insert/',insert,name="insert"),
    path('selectall/',selectAll,name="selectall"),
    path('selectwhere/',selectWhere,name="selectwhere"),
    path('delete/',delete,name="delete"),
    path('update/',update,name="update"),



]
