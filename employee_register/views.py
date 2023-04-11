from django.shortcuts import render,redirect
from . forms import EmployeeForm
from .models import Employee


def employee_list(request):
    employee_list = Employee.objects.all()
    context = {
        'employee_list':employee_list
    }
    return render(request, 'employee_register/main/employee_list.html',context)

#this fxn will be used For GET and POST request
def employee_form(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = EmployeeForm()
        else:
             #we use primay key to filter the object
             employee = Employee.objects.get(pk=id) 
             form = EmployeeForm(instance=employee)
        context = {
            'form':form
        }
        return render(request, 'employee_register/main/employee_form.html', context)
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid(): 
            form.save()
            return redirect('employee_list')

#this fxn will be used for deletion
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_list')