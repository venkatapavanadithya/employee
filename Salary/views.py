from django.shortcuts import redirect, render

from Salary.forms import EmployeeForm
from Salary.models import Employee 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required

# Create your views here.
def home(request):
    employees=Employee.objects.all()
    return render(request,'Salary/home.html',{'employees':employees})

def detail(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'Salary/employee_detail.html',{'employee':employee})
def add_employee(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_success')
    else:
        form=EmployeeForm()
    return render(request,'Salary/add_employee.html',{'form':form})
def success_view(request):
    return render(request,'Salary/success.html')
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'Salary/register.html',{'form':form})