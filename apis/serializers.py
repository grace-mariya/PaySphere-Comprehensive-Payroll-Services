from multiprocessing import Value
from django.forms import IntegerField
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import LeaveManagement, PayrollManagement, User, Employee, Position, UserAnnualSalaryRevision
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__' 



