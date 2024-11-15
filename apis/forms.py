# forms.py
from django import forms
from .models import Employee

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'job_title', 'department', 'hire_date', 'salary']
