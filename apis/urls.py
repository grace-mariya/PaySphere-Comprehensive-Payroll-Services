
from django.urls import path
from . import views
from .views import EmployeeCreateView,EmployeeDetailView


urlpatterns = [
    
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('employees/', EmployeeCreateView.as_view(), name='employee-list-create'),  # For listing and creating employees
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    
]
