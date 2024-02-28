# models.py
from django.db import models

class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=100,unique=True)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_no = models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class Advisor(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    specification = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

class Item(models.Model):
    CATEGORY_CHOICES = (
        ('F','fruit'),
        ('V','vegetable'),
        ('J','junk_food'),
    )
    VITAMIN_CHOICES = (
        ('A','vitamin A'),
        ('C','vitamin C'),
        ('D','vitamin D'),
        ('E','vitamin E'),
        ('K','vitamin K'),
        ('B1','thiamine'),
        ('B2','riboflavin'),
        ('B3','niacin'),
        ('B6','pyridoxine'),
        ('B12','cyanocobalamin'),
        ('B5','Pantothenic acid'),
        ('B7','Biotin '),
        ('B9','Folate'),
    )
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=1,choices=CATEGORY_CHOICES)
    calories = models.IntegerField()
    vitamin = models.CharField(max_length=10,choices=VITAMIN_CHOICES)
    ingredient = models.CharField(max_length=100)
    image = models.ImageField(upload_to='item_images/')

class Report(models.Model):
    pr_nm = models.ForeignKey(Person,on_delete=models.CASCADE,default=1)
    date = models.DateField()
    total_calories = models.IntegerField()
    quentity = models.IntegerField()

class Favorite_list(models.Model):
    pr_name = models.ForeignKey(Person,on_delete=models.CASCADE,default=1)
    item_id = models.ForeignKey(Item,on_delete=models.CASCADE)

# class Target():
    # pr_nm 
    # calories
    # vitamins
    
    
