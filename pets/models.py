
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Status(models.Model):
    status = models.CharField(max_length = 100,blank = False,null = False)
    
    def __str__(self):
        return self.status
    
class Category(models.Model):
    """ type of animal """
    title = models.CharField(max_length = 100,blank = False, null = False)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    """ tags of animal"""
    name = models.CharField(max_length = 100)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name 

#create product(animal) table 
class Animal(models.Model):
    name = models.CharField(max_length = 100,blank = False, null = False)
    about = models.TextField()
    tag = models.ManyToManyField(Tag,null = True)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    species = models.ForeignKey(Category,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User,null = True,related_name = "likes",blank = True)
    img = models.ImageField(blank = True,upload_to = "images/")
    status = models.ForeignKey(Status,on_delete = models.SET_DEFAULT,default = "Unknown")
    price = models.FloatField()
    
    def __str__(self):
        return self.name
    
    @property
    def total_likes(self):
        return self.likes.count() 
    

class Comments(models.Model):
    name = models.CharField(max_length = 100)
    body = models.CharField(max_length = 100)
    dateAdded = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE,blank = True)
    animal = models.ForeignKey(Animal,on_delete = models.CASCADE,blank = True)
    
    def __str__(self):
        return self.name 
