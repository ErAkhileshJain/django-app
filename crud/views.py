from django.shortcuts import render, redirect
from crud.forms import EmployeeForm
from testapp.models import Employee
from django.contrib.auth.decorators import login_required


# Create your views here.


def create(req):
    form = EmployeeForm()
    if req.method == 'POST':
        form = EmployeeForm(req.POST)
        if form.is_valid():
            formData = form.cleaned_data
            emp = Employee()
            emp.emp_name = formData['emp_name']
            emp.emp_email = formData['emp_email']
            emp.emp_address = formData['emp_address']
            emp.save()
            return redirect(index)
    data = {
        'form': form
    }
    return render(req, 'crud/create.html', data)

@login_required(login_url='/signin')
def index(req):
    data = Employee.objects.all()
    return render(req, 'crud/index.html', {'data': data})


def update(req):
    id = req.GET['id']
    data = Employee.objects.get(id=id)
    form = EmployeeForm(instance=data)
    if req.method == 'POST':
        form = EmployeeForm(req.POST, instance=data)
        if form.is_valid():
            formData = form.cleaned_data
            emp = Employee()
            emp.id = id  # if we add this means primary django treat is as update
            emp.emp_name = formData['emp_name']
            emp.emp_email = formData['emp_email']
            emp.emp_address = formData['emp_address']
            emp.save()
            return redirect(index)
    d1 = {'form': form}
    return render(req, 'crud/update.html', d1)


def view(req):
    id = req.GET['id']
    data = Employee.objects.get(id=id)
    return render(req, 'crud/view.html',{'data':data})


def delete(req):
    id = req.GET['id']
    data = Employee.objects.get(id=id)
    data.delete()

    return redirect(index)
