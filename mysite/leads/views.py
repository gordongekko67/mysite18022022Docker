from django.shortcuts import render, redirect  
from  django.http import HttpResponse
from .forms import CaniModelForm
from .models import Cani

def home_page(request):
    return renderHttpResponse("Hello world")

def home(request):
    return render(request,'home.html') 

def Cani_emp(request):  
    if request.method == "POST":  
        form = CaniModelForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/leads/canishow/')  
            except:  
                pass
    else:  
        form = CaniModelForm()  
    return render(request,'caniindex.html',{'form':form})  

def Cani_show(request):  
    canis = Cani.objects.all()  
    return render(request,"canishow.html",{'canis':canis})  

def Cani_edit(request, id):  
    canis = Cani.objects.get(id=id)  
    return render(request,'caniedit.html', {'canis':canis})  

def Cani_update(request, id):  
    canis = Cani.objects.get(id=id)  
    form = CaniForm(request.POST, instance = canis)  
    if form.is_valid():  
        form.save()  
        return redirect("/leads/canishow")  
    return render(request, 'caniedit.html', {'canis': canis})  
    
def Cani_destroy(request, id):  
    canis = Cani.objects.get(id=id)  
    canis.delete()  
    return redirect("/leads/canishow")  