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
            addemp="Employee Added"
            success="success"
            print(addemp)
            return render(request,"emp_list.html",{"flag":success})   
        else:
            error="error"
            print(error)
            return render(request,"emp_create.html",{"form":form,"flag":error})

class ViewEmp(View):
    def get(self,request,*args,**kwargs):
        datas=Employees.objects.all()
        return render(request,"emp_list.html",{"datas":datas})
    def post(self,request,*args,**kwargs):
        id=request.POST.get("box")
        datas=Employees.objects.filter(id=id)
        return render(request,"emp_list.html",{"datas":datas})

class DetailEmp(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        return render(request,"emp_detail.html",{"data":qs})
    
class DeleteEmp(View):
    def get(request,*args,**kwargs):
        id=kwargs.get("pk")
        Employees.objects.get(id=id).delete()
        return redirect("view_emp")

class UpdateEmp(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        form=EmpModelForm(instance=qs)
        return render(request,"emp_update.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        form=EmpModelForm(request.POST,instance=qs)
        if form.is_valid():
            form.save()
            success="success"
            print(success)
            return redirect("detail_emp",pk=id)   
        else:
            error="error"
            print(error)
            return render(request,"emp_update.html",{"form":form,"flag":error})