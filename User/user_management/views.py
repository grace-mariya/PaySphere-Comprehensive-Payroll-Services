from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# User Registration View
def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Log the user in
            messages.success(request, "Registration successful!")
            return redirect('employee_dashboard')  # Redirect to dashboard
    else:
        form = UserRegistrationForm()
    return render(request, 'user_management/user_registration.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('employee_dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'user_management/login.html', {'form': form})

# Employee Dashboard (Requires Login)
@login_required
def employee_dashboard(request):
    return render(request, 'employee/home.html')
