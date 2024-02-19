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
    # CATEGORY_CHOICES = (
    #     ('F','fruits'),
    #     ('V','vegitable'),
    #     ...
    # )
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    calories = models.IntegerField()
    vitamin = models.CharField(max_length=100)
    ingredient = models.CharField(max_length=100)

class Report(models.Model):
    # pr_nm = forenkey()
    date = models.DateField()
    total_calories = models.IntegerField()
    quentity = models.IntegerField()

#class Favorite_list(models.Model):
    # pr_name = models.Forenkey()
    # item_id = models.forenkey()

# class Target():
    # pr_nm 
    # calories
    # vitamins
    
    
