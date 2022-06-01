from django.contrib import admin

from leaveapp.models import Leave, LeaveType, Employee, Role
# Register your models here.

admin.site.register(Leave)
admin.site.register(LeaveType)
admin.site.register(Employee)
admin.site.register(Role)
