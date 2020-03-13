from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.


def index(request):
    tasks = Tasks.objects.all()
    form = TaskForm()    
    context={'tasks':tasks,'form':form}

    if request.method == 'POST':
        form =TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'tasks/list.html',context)


def updateTask(request,id):
    task = Tasks.objects.get(id=id)
    form= TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context={'form':form}
    return render(request,'tasks/update_task.html',context)

def deleteTask(request,id):
    item= Tasks.objects.get(id=id)    
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context={'item':item}        
    return render(request,'tasks/delete_task.html',context)