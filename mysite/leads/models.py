from django.db import models
 
class Agent(models.Model):
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.last_name



class Razze(models.Model):
    nome_razza= models.CharField(max_length=20)
    desc_razza= models.CharField(max_length=20)
    peso_razza= models.IntegerField(default=0)

    def __str__(self):
        return self.desc_razza


class Cani(models.Model):
    nome_cane = models.CharField(max_length=20, null=True,  blank=True)
    razza_cane = models.ForeignKey("Razze", null=True, blank=True, on_delete=models.SET_NULL)
    class Meta:  
        db_table = "cani" 

    def __str__(self):
        return f"{self.nome_cane} {self.razza_cane}"

