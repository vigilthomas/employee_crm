from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from crm.form import *
from crm.models import *
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


def login_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"Please Login to Access the data....")
            return redirect('auth_login')
        else:
            return fn(request,*args,**kwargs)
    return wrapper

decs=[login_required,never_cache]

# Create your views here.

class SigninView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            passwd = form.cleaned_data.get("password")
            user_obj = authenticate(request, username=uname, password=passwd)
            if user_obj:
                print(User, "Found")
                login(request,user_obj)
                print(request.user)
                return redirect('home')
        
        messages.error(request, "Invalid Input ..")
        print("error")
        return render(request, "login.html", {"form": form})

class SignoutView(View):
    def get(self, request, *args, **kwargs):
        print(request.user)
        logout(request)
        print(request.user)
        return redirect('auth_login')


class SignupView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, "register.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            User.objects.create_user(**form.cleaned_data)
            messages.success(request, " User Created Successfully..")
            print("Success")
            return redirect("auth_login")

        else:
            messages.error(request, "Failed to create user..")
            print("error")
            return render(request, "register.html", {"form": form})

@method_decorator(decs,name="dispatch")
class ViewHome(View):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')


@method_decorator(decs, name="dispatch")
class ViewAddEmp(View):
    def get(self,request,*args,**kwargs):
        form=EmpModelForm()
        return render(request,"emp_create.html",{"form":form})   
    def post(self,request,*args,**kwargs):
        form=EmpModelForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request," Employee Added Successfully..")
            print("Success")
            return redirect("view_emp")
        else:
            messages.error(request,"Failed to Add Employee..")
            print("error")
            return render(request,"emp_create.html",{"form":form})


@method_decorator(decs, name="dispatch")
class ViewEmpList(View):
    def get(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        departments=Employees.objects.all().values_list("department",flat=True).distinct()
        print(departments)
        if "department" in request.GET:
            dept = request.GET.get("department")
            qs=qs.filter(department__iexact=dept)
            
        return render(request, "emp_list.html", {"datas": qs, "departments": departments})
    def post(self,request,*args,**kwargs):
        name=request.POST.get("box")
        datas=Employees.objects.filter(name__icontains=name)
        return render(request,"emp_list.html",{"datas":datas,'name':name})


@method_decorator(decs, name="dispatch")
class ViewEmpDetail(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        return render(request,"emp_detail.html",{"data":qs})


@method_decorator(decs, name="dispatch")
class ViewEmpDelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employees.objects.get(id=id).delete()
        messages.success(request," Employee Deleted Successfully..")
        return redirect("view_emp")


@method_decorator(decs, name="dispatch")
class ViewEmpUpdate(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        form=EmpModelForm(instance=qs)
        return render(request,"emp_update.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        form = EmpModelForm(request.POST,files=request.FILES, instance=qs)
        if form.is_valid():
            form.save()
            messages.success(request," Employee Updated Successfully..")
            print("success")
            return redirect("detail_emp",pk=id)   
        else:
            print("error")
            messages.error(request," Failed to Update Employee Details..")
            return render(request,"emp_update.html",{"form":form})
