from django.contrib import admin

from curdapp.models import StudentData



class AdminStudentData(admin.ModelAdmin):
    list_display = ['student_roll_no', 'student_first_name', 'student_last_name']

admin.site.register(StudentData,AdminStudentData)

