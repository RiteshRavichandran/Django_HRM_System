from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    #path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("company/<int:pk>", views.company_record, name="company"),
    path("employee/<int:pk>", views.employee_record, name="employee"),
]
