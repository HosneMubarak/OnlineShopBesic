from django.urls import path
from .views import EmployeeRegistrationView, CustomerRegistrationView, RegistrationView, login_view, logout_view, \
    user_profile

app_name = 'account'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('customer_registration/', CustomerRegistrationView.as_view(), name='customer_registration'),
    path('employee_registration/', EmployeeRegistrationView.as_view(), name='employee_registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user_profile/', user_profile, name='user_profile'),
]
