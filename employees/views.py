from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def employee_list(request):
    query = request.GET.get('q')

    if query:
        employees = Employee.objects.filter(name__icontains=query)
    else:
        employees = Employee.objects.all()

    return render(request, 'employees/employee_list.html', {
        'employees': employees
    })

@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'employees/add_employee.html', {'form': form})

@login_required
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/update_employee.html', {'form': form})


@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

    return render(request, 'employees/delete_employee.html', {'employee': employee})

def user_logout(request):
    logout(request)
    return redirect('/accounts/login/')