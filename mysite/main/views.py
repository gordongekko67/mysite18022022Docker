from django.shortcuts import render, redirect  
from .forms import Impiegati22Form  
from .models import Impiegati22
# Create your views here.  

def home(request):
    return render(request,'home.html') 

def emp(request):  
    if request.method == "POST":  
        form = Impiegati22Form(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = Impiegati22Form()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Impiegati22.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Impiegati22.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Impiegati22.objects.get(id=id)  
    form = Impiegati22Form(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Impiegati22.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  