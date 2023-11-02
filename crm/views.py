from django.shortcuts import render
from django.views import View
from crm.form import *
from crm.models import Employees
# Create your views here.


class Index(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class AddEmp(View):
    def get(self,request,*args,**kwargs):
        form=EmpForm()
        return render(request,"emp_create.html",{"form":form})   
    def post(self,request,*args,**kwargs):
        flag=False
        form=EmpForm(request.POST)
        if form.is_valid():
            Employees.objects.create(**form.cleaned_data)
            book="Book Added"
            flag=True
            print(book)
        return render(request,"emp_list.html",{"form":form,"flag":flag})

class ViewEmp(View):
    def get(self,request,*args,**kwargs):
        datas=Employees.objects.all()
        return render(request,"emp_list.html",{"datas":datas})

class UpdateEmp(View):
    def get(self,request,*args,**kwargs):
        form=EmpForm()
        return render(request,"emp_update.html",{"form":form})   
    def post(self,request,*args,**kwargs):
        form=EmpForm(request.POST)
        return render(request,"emp_list.html",{"form":form})