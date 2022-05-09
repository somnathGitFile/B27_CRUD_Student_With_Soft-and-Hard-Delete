from urllib import request
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login_url')
def studentFormView(request):
    form = StudentForm()
    template_name = 'crud/studentform.html'
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showstu_url')
    context ={'form':form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def showstudentView(request, page=1):
    data = Student.objects.filter(status=True)
    template_name = 'crud/showstudents.html'
    paginator = Paginator(data, 2)
    try:
        data = paginator.page(page)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {'obj': data}
    return render(request, template_name, context)

def updateStuView(request, id):
    data = Student.objects.get(id=id)
    form = StudentForm(instance=data)
    template_name = 'crud/studentform.html'
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('showstu_url')
    context = {'form': form}
    return render(request, template_name,context)

def softdeleteStuview(request, id):
    obj = Student.objects.get(id=id)  #(primarykey_col_name=parameter_name)
    template_name = 'crud/confirmation.html'
    context = {'obj': obj}
    if request.method == 'POST':
        obj.status = False
        obj.save()
        return redirect('showstu_url')
    
    return render(request, template_name, context)


def showdeletestudentView(request, page=1):
    data = Student.objects.filter(status=False)
    template_name = 'crud/deletedstudents.html'
    paginator = Paginator(data, 2)
    try:
        data = paginator.page(page)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {'obj': data}
    return render(request, template_name, context)


def restorestudentView(request, id):
    obj = Student.objects.get(id=id)  #(primarykey_col_name=parameter_name)
    obj.status = True
    obj.save()
    return redirect('showstu_url')
    
'''
def restorestudentView(request, id):
    obj1 = Student.objects.get(id=id) #(primarykey_col_name=parameter_name)
    form = StudentForm(instance=obj1)
    template_name = 'crud/studentform.html'
    
    context = {'form': form}
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj1)
        if form.is_valid():
            form.save()
            return redirect('showstu_url')

    return render(request, template_name, context)

    '''


def HarddeleteView(request, id):
    obj = Student.objects.get(id=id)  #(primarykey_col_name=parameter_name)
    template_name = 'crud/harddeletconf.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('showstu_url')
    
    return render(request, template_name)

