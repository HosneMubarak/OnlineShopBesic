from django.contrib import admin
from .models import CustomUser, Employee, Customer

admin.site.register(CustomUser)
admin.site.register(Employee)
admin.site.register(Customer)
