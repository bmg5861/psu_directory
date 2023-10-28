from django.shortcuts import render, redirect
from directory.forms import StaffForm
from directory.models import Staff
from django import forms

def staf(request):  
    if request.method == "POST":  
        form = StaffForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:   
        return redirect('/show')
def show(request):  
    staffs = Staff.objects.all()  
    return render(request,"show.html",{'staffs':staffs})  
def edit(request, id):  
    staff = Staff.objects.get(id=id)  
    return render(request,'edit.html', {'staff': staff})  
def update(request, id):  
    staff = Staff.objects.get(id=id)
    form = StaffForm(request.POST, request.FILES, instance = staff)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'staff': staff})  
def destroy(request, id):  
    staff = Staff.objects.get(id=id)  
    staff.delete()  
    return redirect("/show")  