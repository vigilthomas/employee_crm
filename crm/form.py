from django import forms


class EmpForm(forms.Form):
    name=forms.CharField(label="Employee Name ",widget=forms.TextInput(attrs={"class":"form-control m-2"}))    
    department=forms.CharField(label="Department Name ",widget=forms.TextInput(attrs={"class":"form-control m-2"}))
    email=forms.EmailField(label="Email ",widget=forms.TextInput(attrs={"class":"form-control m-2"}))
    phone=forms.IntegerField(label="Phone ",widget=forms.TextInput(attrs={"class":"form-control m-2"}))
    age=forms.IntegerField(label="Age ",widget=forms.TextInput(attrs={"class":"form-control m-2"})) 
    salary=forms.IntegerField(label="Salary ",widget=forms.TextInput(attrs={"class":"form-control m-2"}))
  

# widget=forms.EmailField(attrs={"class":"form-control w-50"})