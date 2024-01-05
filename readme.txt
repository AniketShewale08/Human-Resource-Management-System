# HRMS (Human Resource Management System)

Welcome to the HRMS (Human Resource Management System), a Django-based web application for managing employee information, attendance tracking, and basic reporting.

## Project Structure

- HRMS (Human Resource Management System) : Django project settings and configuration.
- employees/: Django app for managing employees.
    - migrations/: Database migration files.
    - static/: Static files (CSS, JS).
        - css/: CSS stylesheets.
    - templates/: HTML templates.
    - views.py: Views and API endpoints.
    - models.py: Database models.
    - serializers.py: Serializers for data serialization.
    - urls.py: URL patterns for the app.
- manage.py: Django management script.

## Features

- Home Page: Display the list of employees.
- Add Employee API: Endpoint to add a new employee.
- Employee List API: Endpoint to retrieve the list of all employees.
- Mark Attendance API: Endpoint to mark attendance for a specific employee on a given date.
- Attendance Details API: Endpoint to retrieve attendance details for a specific employee.
- Department Report: Route to show a simple report with the count of employees in each department.

## How to Run Locally

1. Install Python and Django:

   pip install django

2. Create and apply database migrations:
	
   python manage.py makemigrations
   python manage.py migrate

3. Run the development server:
   
   python manage.py runserver

4. Access the app in your web browser at http://127.0.0.1:8000/



-------Example API Endpoints--------

Add Employee:

Endpoint: POST /add_employee/
Request Body:
	{
    	"name": "John Doe",
    	"designation": "Software Engineer",
    	"department": "Engineering",
    	"date_of_joining": "2022-01-10"
	}


Employee List:

Endpoint: GET /employees/
Response: List of all employees.
Mark Attendance:

Endpoint: POST /mark_attendance/<employee_id>/
Request Body:

	{
	    "date_of_attendance": "2022-01-15"
	}


Attendance Details:
    Endpoint: GET /attendance_details/<employee_id>/
    Response: Attendance details for the specified employee.
    
Department Report:

Route: /department_report/
Displays a report with the count of employees in each department.




