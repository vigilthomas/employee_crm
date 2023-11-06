from django.shortcuts import render,redirect
from django.views import View
from crm.form import *
from crm.models import *
# Create your views here.


class Index(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class AddEmp(View):
    def get(self,request,*args,**kwargs):
        form=EmpModelForm()
        return render(request,"emp_create.html",{"form":form})   
    def post(self,request,*args,**kwargs):
        form=EmpModelForm(request.POST)
        if form.is_valid():
            form.save()
            book="Employee Added"
            success="success"
            print(book)
            return render(request,"emp_list.html",{"flag":success})   
        else:
            error="error"
            print(error)
            return render(request,"emp_create.html",{"form":form,"flag":error})

class ViewEmp(View):
    def get(self,request,*args,**kwargs):
        datas=Employees.objects.all()
        return render(request,"emp_list.html",{"datas":datas})

class DetailEmp(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        return render(request,"emp_detail.html",{"data":qs})

class UpdateEmp(View):
    def get(self,request,*args,**kwargs):
        form=EmpModelForm()
        return render(request,"emp_update.html",{"form":form})   
    def post(self,request,*args,**kwargs):
        form=EmpModelForm(request.POST)
        return render(request,"emp_list.html",{"form":form})