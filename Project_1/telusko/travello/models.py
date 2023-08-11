from django.db import models

# Create your models here.

class Destination(models.Model):
    id = models.IntegerField(primary_key=True)
    name= models.CharField(max_length=25)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)
