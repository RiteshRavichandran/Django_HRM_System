from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

class Employee(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=10, unique=True)  # Change to CharField
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    