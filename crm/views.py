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
        form=EmpForm(request.POST)
        if form.is_valid():
            Employees.objects.create(**form.cleaned_data)
            print("Done")

        return render(request,"emp_list.html",{"form":form})
class ViewEmp(View):
    def get(self,request,*args,**kwargs):
        datas=Employees.objects.all()
        return render(request,"emp_list.html",{"datas":datas})