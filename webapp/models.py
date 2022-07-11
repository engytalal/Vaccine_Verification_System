
from django.db import models


# Create your models here.
class employee(models.Model):
    
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    Na_id=models.IntegerField(unique=True)
    country=models.CharField(max_length=50, null=False, blank=False)
    phone_num=models.IntegerField()
    email=models.EmailField()
    password=models.SlugField(max_length=50, unique=True)


    def __str__(self):
        return self.firstname
    class meta:
        ordering =['name']


class user(models.Model):

    name=models.CharField(max_length=50)
    age=models.IntegerField()
    Na_id=models.IntegerField(unique=True)
    country=models.CharField(max_length=50, null=False, blank=False)
    address=models.SlugField(max_length=50,unique=False)
    phone_num=models.IntegerField()



    def __str__(self):
        return self.name
    class meta:
        ordering =['name']