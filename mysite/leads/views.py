from django.shortcuts import render, redirect  
from  django.http import HttpResponse
from .forms import CaniModelForm
from .models import Cani

def home_page(request):
    return renderHttpResponse("Hello world")

def home(request):
    return render(request,'home.html') 

#immissione nuovo record 
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

#visualizzazione records 
def Cani_show(request):  
    canis = Cani.objects.all()  
    return render(request,"canishow.html",{'canis':canis})  

#modifica records 
def Cani_edit(request,id):  
    if request.method == "POST":  
        cani = Cani.objects.get(id=id)  
        form = CaniModelForm(request.POST, instance = cani)  
        form.id = id
        if form.is_valid():  
             form.save()  
        return redirect("/leads/canishow")   
          
    else:  
        canis = Cani.objects.get(id=id)  
        form = CaniModelForm(instance = canis)  
        form.id = id 
    return render(request,'caniindex2.html',{'form':form})  


def Cani_update(request, id):  
    cani = Cani.objects.get(id=id)  
    form = CaniModelForm(request.POST, instance = cani)  
    form.id = id
    if form.is_valid():  
        form.save()  
        return redirect("/leads/canishow")  
    
      
    
def Cani_destroy(request, id):  
    canis = Cani.objects.get(id=id)  
    canis.delete()  
    return redirect("/leads/canishow")  