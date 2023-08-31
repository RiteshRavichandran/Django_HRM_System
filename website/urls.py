from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("company/<int:pk>", views.company_record, name="company"),
    path("employee/<int:pk>", views.employee_record, name="employee"),
    path("delete_employee/<int:pk>", views.delete_employee_record, name="delete_employee"),
    path("add_company/", views.add_company_record, name="add_company"),
    path("add_employee/", views.add_employee_record, name="add_employee"),
    path("update_company/<int:pk>", views.update_company_record, name="update_company"),
    path("update_employee/<int:pk>", views.update_employee_record, name="update_employee"),
]
