from django.shortcuts import redirect, render
from employee.models import Employee
from employee.forms import EmployeeForm
# Create your views here


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass

    else:
        form = EmployeeForm()
        return render(request, 'index.html', {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, 'show.html', {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)
    print(form)
    return render(request, 'edit.html', {'employee': employee, 'form': form})


def update(request, id):
    print(id)
    employee = Employee. objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)

    if form.is_valid():
        print(form)
        form.save()
        return redirect("/show")
    else:
        print(form.errors)


    return render(request, 'edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee. objects.get(id=id)
    employee.delete()
    return redirect("/show")
