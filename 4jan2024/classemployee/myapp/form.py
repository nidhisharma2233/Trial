from django import forms
class Employee(forms.Form):
    name = forms.CharField(max_length=100)
    mail = forms.EmailField(max_length=100)
    department = forms.CharField(max_length=100)
    position = forms.CharField(max_length=100)
