from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Employee
from django.db import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer


# Create your views here.

def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees' : employees})


@api_view(['POST'])
def add_employee(request):
    if request.method == "POST":
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Employee added successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def employee_list(request):
    employees = Employee.objects.all()
    employee_list = [{'name' : emp.name, 'designation': emp.designation, 'department' : emp.department} for emp in employees]
    return JsonResponse({'employees' : employee_list})

@api_view(['POST'])
def mark_attendance(request, employee_id):
    employee = get_object_or_404(Employee, pk = employee_id)
    date_of_attendance = request.data.get('date_of_attendance')

    if not date_of_attendance:
        return Response({"error" : "Date of attendance is required."})
    
    employee.attendance = True
    employee.attendance_date = date_of_attendance
    employee.save()
    return Response({'message' : f'Attendance marked for {employee.name} on {date_of_attendance}.'})
@api_view(["GET"])
def attendance_details(request, employee_id):
    employee = get_object_or_404(Employee, pk = employee_id)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)

def department_report(request):
    department_counts = Employee.objects.values('department').annotate(count=models.Count('department'))
    return render(request, 'department_report.html', {'department_counts' : department_counts})

