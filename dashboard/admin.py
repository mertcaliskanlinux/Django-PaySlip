from django.contrib import admin
from .models import Grade,Staff
from dashboard import models
# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','gross_salary')


class GradeAdmin(admin.ModelAdmin):
    list_display = ('position','basic_salary')

admin.site.register(Grade,GradeAdmin)
admin.site.register(Staff,StaffAdmin)