from django import forms


class EmpForm(forms.Form):
    name = forms.CharField(label="Employee Name ")
    department=forms.CharField(label="Department Name ")
    email=forms.EmailField(label="Email ")
    phone=forms.IntegerField(label="Phone ")
    age=forms.IntegerField(label="Age ") 
    salary=forms.IntegerField(label="Salary ")
  

# widget=forms.EmailField(attrs={"class":"form-control w-50"})