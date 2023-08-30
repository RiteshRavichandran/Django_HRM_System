from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Company, Employee


def home(request):
    companies = Company.objects.all()
    employees = Employee.objects.all()

    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            messages.success(request, "Incorrect Credentials")
            return redirect('home')
    else:
        return render(request, "home.html", {'companies':companies, 'employees':employees})


def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful!")
    return redirect('home')


def company_record(request, pk):
    if request.user.is_authenticated:
        # Look up Records
        company_record = Company.objects.get(id=pk)
        return render(request, "company_record.html", {'company_record':company_record})
    else:
        messages.success(request, "You must be Logedin to view that page")
        return redirect('home')


def employee_record(request, pk):
    if request.user.is_authenticated:
            # Look up Records
            employee_record = Employee.objects.get(id=pk)
            return render(request, "employee_record.html", {'employee_record':employee_record})
    else:
        messages.success(request, "You must be Logedin to view that page")
        return redirect('home')
    

def delete_employee_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Employee.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be Logedin to delete the records")
        return redirect('home')
    

def add_company_record(request):
    return render(request, "add_company_record.html", {})

def add_employee_record(request):
    return render(request, "add_employee_record.html", {})