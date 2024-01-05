from django.urls import path
from .views import (home, add_employee, employee_list,
                    mark_attendance, attendance_details, 
                    department_report
                    )
urlpatterns = [
    path('', home, name = 'home'),
    path('add_employee/', add_employee,name = 'add_employee'),
    path('employee_list/', employee_list,name = 'employee_list'),
    path('mark_attendance/<int:employee_id>/', mark_attendance,name = 'mark_attendance'),
    path('attendance_details/<int:employee_id>/', attendance_details,name = 'attendance_details'),
    path('department_report/', department_report,name = 'department_report'),
]
