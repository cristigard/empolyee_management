from enum import unique
from lzma import MODE_NORMAL
from pyexpat import model
from re import T
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings



class Role(models.Model):
    name = models.CharField(max_length=50)

    def get_update_url(self):
        return reverse('update-role', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('delete-role', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name}'



class Employee(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete=models.SET_DEFAULT, default=None,)
    manager = models.ForeignKey('self', null=True, blank = True, on_delete = models.SET_NULL)
    employment_date = models.DateField()
    cim = models.IntegerField("CIM", unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank = True, on_delete = models.CASCADE)

    class Meta:
        ordering = ['cim']

    def get_absolute_url(self):
        return reverse('employee-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('employee-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('employee-delete', kwargs={'pk': self.pk})
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Files(models.Model):
    file = models.FileField(upload_to='uploads/', unique=True)
    file_name = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def get_delete_url(self):
        return reverse('delete-file', kwargs={'pk': self.pk})


    def __str__(self):
        return f'{self.file}'




class Group(models.Model):
    name = models.CharField(max_length=128, unique=True)
    members = models.ManyToManyField(Employee, through='Membership')

    def get_update_url(self):
        return reverse('update-group', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('delete-group', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()

    
    def get_absolute_url(self):
        return reverse('employee-list')

    def get_delete_url(self):
        return reverse('membership-delete', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.employee.first_name} {self.employee.last_name} from {self.group.name}'
        
    #restrict an employee to be in the same group multiple time
    class Meta:
        unique_together = [['employee','group']]



class DeletedEmployee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=100)
    manager = models.CharField(max_length=100, blank = True)
    cim = models.IntegerField()
    employment_date = models.DateField()
    deleted_date = models.DateField(auto_now=True)