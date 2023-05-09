from django.contrib import admin

# Register your models here.
from .models import Admin, Employee, AccountHolder

admin.site.register(Admin)
admin.site.register(Employee)
admin.site.register(AccountHolder)