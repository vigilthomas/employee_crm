from django import forms
from crm.models import *

class EmpModelForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields="__all__"
        widgets={
            'name' :forms.TextInput(attrs={"class":"form-control"}),
            'department' :forms.TextInput(attrs={"class":"form-control"}),
            'email' :forms.TextInput(attrs={"class":"form-control"}),
            'phone' :forms.TextInput(attrs={"class":"form-control"}),
            'age' :forms.TextInput(attrs={"class":"form-control"}),
            'salary' :forms.TextInput(attrs={"class":"form-control"})
        }