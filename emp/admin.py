from django.contrib import admin
from emp.models import Employee, Group, Membership

# Register your models here.
admin.site.register(Employee)
admin.site.register(Group)
admin.site.register(Membership)