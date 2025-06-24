from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('joined_date')
    serializer_class = EmployeeSerializer


def employee_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        joined_date = request.POST.get('joined_date')

        # Create new Employee
        Employee.objects.create(
            name=name,
            email=email,
            address=address,
            department=department,
            joined_date=joined_date
        )
        return redirect('employee-list')

    return render(request, 'register.html')


def employee_list(request):
    # Fetch all employees
    employees = Employee.objects.all().order_by('joined_date')
    return render(request, 'employees.html', {
        'employees': employees
    })


def employee_edit(request, pk):
    """
    Render and process edit form for existing employee.
    Template: register.html (reused)
    """
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.address = request.POST.get('address')
        employee.department = request.POST.get('department')
        employee.joined_date = request.POST.get('joined_date')
        employee.save()
        return redirect('employee-list')

    return render(request, 'register.html', {'employee': employee})


def employee_delete(request, pk):
    """
    Delete the specified employee and redirect to list.
    """
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee-list')
