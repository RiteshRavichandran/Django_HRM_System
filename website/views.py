from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCompanyRecordForm, AddEmployeeRecordForm
from .models import Company, Employee
import re



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
            messages.success(request, "Incorrect Credentials...")
            return redirect('home')
    else:
        return render(request, "home.html", {'companies':companies, 'employees':employees})


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


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
    form = AddCompanyRecordForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_form = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, "add_company_record.html", {'form':form})
    else:
        messages.success(request, "You must be Logedin to add the records")
        return redirect('home')

def add_employee_record(request):
    form = AddEmployeeRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                employee_id = form.cleaned_data['employee_id']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                contact_number = form.cleaned_data['contact_number']
                email = form.cleaned_data['email']

                if not re.match(r'^e\d*$', employee_id):
                    form.add_error('employee_id', "Employee ID must start with 'e' followed by digits.")

                elif not re.match(r'^[A-Za-z\.]*$', first_name):
                    form.add_error('first_name', "First Name cannot contain number or special characters except (.)")

                elif not re.match(r'^[A-Za-z\.]*$', last_name):
                    form.add_error('last_name', "Last Name cannot contain number or special characters except (.)")

                elif not re.match(r'^\d{10}$', contact_number):
                    form.add_error('contact_number', "Contact Number cannot contain alphabets or special characters, should be exactly 10 characters")
                
                elif not email.endswith('.com') or '@' not in email:
                     form.add_error('email', "Email ID should have \"@\" symbol in between and \".com\" at the end)")
                
                else:
                    add_form = form.save()
                    messages.success(request, "Record Added...")
                    return redirect('home')
                
        return render(request, "add_employee_record.html", {'form':form})
    
    else:
        messages.success(request, "You must be Logedin to add the record")
        return redirect('home')


def update_company_record(request, pk):
    if request.user.is_authenticated:
        current_record = Company.objects.get(id=pk)
        form = AddCompanyRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Company credentials are updated! ")
            return redirect('home')
        
        return render(request, "update_company_record.html", {'form':form})

    else:
        messages.success(request, "You must be Logedin to update the record")
        return redirect('home')


def update_employee_record(request, pk):
    if request.user.is_authenticated:
        current_record = Employee.objects.get(id=pk)
        form = AddEmployeeRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee credentials are updated! ")
            return redirect('home')
        
        return render(request, "update_employee_record.html", {'form':form})

    else:
        messages.success(request, "You must be Logedin to update the record")
        return redirect('home')