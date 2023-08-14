from django.db import models

# Create your models here.

class Cars(models.Model):
    img = models.ImageField()
    cars_name = models.CharField(max_length=64)
    kms = models.IntegerField()
    color = models.TextField(max_length=64)
    maintance = models.TextField(max_length=64)


    def __str__(self) :
        return f'{self.cars_name} color : {self.color}'
    


class about(models.Model) :
    header = models.CharField(max_length=64)    
    parag1 = models.TextField()    
    parag2 = models.TextField(blank = True)    


    def __str__(self) -> str:
        return f"matn about {self.header}"    
    
class Contact(models.Model) :
    name =models.CharField(max_length=64)  
    name_owner =models.CharField(max_length=64)  
    parag1 =models.TextField(blank = True) 
    parag2 =models.TextField(blank = True)    
    number1 =models.TextField(blank = True)    
    number2 =models.TextField(blank = True)    


    def __str__(self) :
        return f"{self.name} , {self.name_owner} "
   

class Home(models.Model) :
    imgone = models.ImageField(blank=True)
    nameone = models.CharField(max_length=64)
    paragone =models.TextField()   
    imgtwo = models.ImageField(blank=True)
    nametwo = models.CharField(max_length=64)
    paragtwo =models.TextField()   
    imgthree = models.ImageField(blank=True)
    namethree = models.CharField(max_length=64)
    paragthree =models.TextField() 
    paragerafe_asli = models.TextField(blank=True)  