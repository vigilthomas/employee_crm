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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from crm.views import *

urlpatterns = [
    path('', SigninView.as_view(), name="auth_login"),
    path('auth/signout', SignoutView.as_view(), name="auth_logout"),
    path('auth/signup', SignupView.as_view(), name="auth_signup"),
    path('home', ViewHome.as_view(), name="home"),
    path('employee/addemp/', ViewAddEmp.as_view(), name="add_emp"),
    path('employee/list/all', ViewEmpList.as_view(), name="view_emp"),
    path('employee/<int:pk>/details/', ViewEmpDetail.as_view(), name="detail_emp"),
    path('employee/<int:pk>/delete/', ViewEmpDelete.as_view(), name="delete_emp"),
    path('employee/<int:pk>/update/',ViewEmpUpdate.as_view(), name="update_emp")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
