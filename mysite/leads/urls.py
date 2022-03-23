from django.contrib import admin  
from django.urls import path  
from . import views  

urlpatterns = [
    
    path('', views.home),  
    path('caniemp/', views.Cani_emp),  
    path('canishow/',views.Cani_show),  
    path('canieditold/<int:id>', views.Cani_editold),  
    path('caniedit/<int:id>', views.Cani_edit), 
    path('caniupdate/<int:id>', views.Cani_update),  
    path('canidelete/<int:id>', views.Cani_destroy),  
    
]      
