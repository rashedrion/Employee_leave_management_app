from datetime import date
from django.db import models
from django.shortcuts import get_object_or_404

# Create your models here.

class ModelMethods():
    created_at = models.DateField(auto_now_add=True)


    @classmethod
    def fetch_all_data(cls):
        return cls.objects.all()

    @classmethod
    def fetch_single_data(cls, id):
        return get_object_or_404(cls, id=id)

    @classmethod
    def delete_single_data(cls, id):
        return cls.fetch_single_data(id).delete()



class Role(ModelMethods, models.Model):
    role_title = models.CharField(max_length=100, verbose_name="Role")
    role_description = models.TextField(blank=True)

    def __str__(self):
        return self.role_title


class Employee(ModelMethods, models.Model):
    name = models.CharField(max_length=150, verbose_name="Full names")
    email = models.EmailField(blank=True)
    date_of_birth = models.DateField(blank=True)
    address = models.CharField(max_length=250, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

 
class LeaveType(ModelMethods, models.Model):
    name = models.CharField(max_length=100, verbose_name="Leave")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Leave(ModelMethods, models.Model):
    STATUS = (
        ('APPROVED', 'Approved'),
        ('REJECTED','Rejected'),
        ('PENDING', 'Pending')
    )

    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS, default="PENDING")
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    requested_days = models.IntegerField(default=1, blank=True)
    applied_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee.name} - {self.type.name}'

