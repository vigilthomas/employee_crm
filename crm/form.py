from django import forms
from django.contrib.auth.models import User
from crm.models import *


class EmpModelForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", 'placeholder': "Ex. Adam John"}),
            'department': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.TextInput(attrs={"class": "form-control"}),
            'phone': forms.TextInput(attrs={"class": "form-control"}),
            'age': forms.TextInput(attrs={"class": "form-control"}),
            'salary': forms.TextInput(attrs={"class": "form-control"}),
            'profile_pic': forms.FileInput(attrs={"class": "form-control"})
        }
        labels = {
            'name': 'Full Name '
        }


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "first_name,last_name,username,email,password"
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control", 'placeholder': "Ex. Adam John"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'password': forms.PasswordInput(attrs={"class": "form-control"}),

        }
