"""
URL configuration for EMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App.views import *

urlpatterns = [
    path('', login_page, name='login_page'),
    path('home/', home_page, name='home_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('register/', register_page, name='register_page'),
    path('dashboard/', dashboard_page, name='dashboard_page'),
    path('singleemployee/<id>/', singleemployee_page, name='singleemployee_page'),
    path('addnewemployee/', addnewemp_page, name='addnewemployee_page'),
    path('updateemployee/<id>/', udateemployee_page, name='updateemployee_page'),
    path('delete_emp/<id>/', delete_emp, name="delete_emp"),
    path('admin/', admin.site.urls),
]
