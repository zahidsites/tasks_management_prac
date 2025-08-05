from django.shortcuts import redirect, render
from tasks.forms import taskFormModel, taskDetailsModel
from django.contrib import messages
from tasks.models import Task
# Create your views here.
def manager(request):
    task = Task.objects.all()
    context = {
        'tasks' : task
    }
    return render(request, 'manager.html', context)

def user(request):
    return render(request, 'user.html')

def taskForm(request):
    form = taskFormModel()
    form2 = taskDetailsModel()
    if request.method == 'POST':
        form = taskFormModel(request.POST)
        form2 = taskDetailsModel(request.POST)
        if form.is_valid() and form2.is_valid():
            task = form.save()
            task2 = form2.save(commit=False)
            task2.task = task
            task2.save()
            messages.success(request, 'Succesfull')
            return redirect('taskForm')
            
    return render(request, 'form/task.html', {"form":form, "form2":form2})


def update_task(request,id):
    task = Task.objects.get(id=id)
    form = taskFormModel(instance=task)
    if task.details:
        form2 = taskDetailsModel(instance=task.details)
    if request.method == 'POST':
        form = taskFormModel(request.POST, instance=task)
        form2 = taskDetailsModel(request.POST, instance=task.details)
        if form.is_valid() and form2.is_valid():
            task = form.save()
            task2 = form2.save(commit=False)
            task2.task = task
            task2.save()
            messages.success(request, 'Succesfull')
            return redirect('update-task',id)
            
    return render(request, 'form/task.html', {"form":form, "form2":form2})

def delete_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        messages.success(request,'Delete successful')
        return redirect('manager')



