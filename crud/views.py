from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def homepage(r):
    emp=Emplyee.objects.all();
    context={
        'emp':emp
    }
    return render(r, 'index.html',context)

def add(r):
    if r.method=='POST':
        name=r.POST.get('name')
        email=r.POST.get('email')
        address=r.POST.get('address')
        phone=r.POST.get('phone')
        emp=Emplyee(
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        emp.save()
        return redirect(homepage)

    return render(r, 'addEmplyee.html')

def edit(r,id):
    emplyee=Emplyee.objects.get(id=id)
    if r.method=='POST':
        name=r.POST.get('name')
        email=r.POST.get('email')
        address=r.POST.get('address')
        phone=r.POST.get('phone')
        emp=Emplyee(
            name=name,
            email=email,
            address=address,
            phone=phone,
            instance=emplyee
        )
        emp.save()
        return redirect(homepage)
    context={
        'emp':emp
    }
    
    return render(r, 'edit.html',context)