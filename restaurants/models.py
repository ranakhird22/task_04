from django.db import models



class Resturant(models.Model):

	name=models.CharField(max_length=20)
	description=models.TextField()
	opening_time =models.CharField(max_length=40)
	closing_time=models.CharField(max_length=40)
	  #def __str__(self) :
      

      #return self.name
# Create your models here.
 

# Create your models here.
   


