"""
URL configuration for employee_crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from crm import views

urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('emp/add/', views.AddEmp.as_view(), name="add_emp"),
    path('emp/list/', views.ViewEmp.as_view(), name="view_emp"),
    path('emp/<int:pk>/details/', views.DetailEmp.as_view(), name="detail_emp"),
    path('emp/<int:pk>/delete/', views.DeleteEmp.as_view(), name="delete_emp"),
    path('emp/<int:pk>/update/', views.UpdateEmp.as_view(), name="update_emp")

]
