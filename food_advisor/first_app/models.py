# models.py
from django.db import models
from multiselectfield import MultiSelectField

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
    def __str__(self):
        return self.name

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
    def __str__(self):
        return self.item_name

class Report(models.Model):
    pr_nm = models.ForeignKey(Person,on_delete=models.CASCADE,default=1)
    date = models.DateField()
    total_calories = models.IntegerField()
    total_vitamins = models.CharField(max_length=200)
    consumed_items = models.CharField(max_length=200)
    total_ingredient = models.CharField(max_length=200)

class Favorite_list(models.Model):
    pr_name = models.ForeignKey(Person,on_delete=models.CASCADE,default=1)
    item_id = models.ForeignKey(Item,on_delete=models.CASCADE)

class Eaten(models.Model):
    pr_name = models.ForeignKey(Person,on_delete=models.CASCADE,default=1)
    item_id = models.ForeignKey(Item,on_delete=models.CASCADE)
    quntity = models.IntegerField()


class Target(models.Model):
    pr_nm = models.ForeignKey(Person, on_delete=models.CASCADE, default=1)
    tr_calories = models.IntegerField()
    VITAMIN_CHOICES = (
        ('A', 'vitamin A'),
        ('C', 'vitamin C'),
        ('D', 'vitamin D'),
        ('E', 'vitamin E'),
        ('K', 'vitamin K'),
        ('B1', 'thiamine'),
        ('B2', 'riboflavin'),
        ('B3', 'niacin'),
        ('B6', 'pyridoxine'),
        ('B12', 'cyanocobalamin'),
        ('B5', 'Pantothenic acid'),
        ('B7', 'Biotin'),
        ('B9', 'Folate'),
    )
    tr_vitamins = MultiSelectField(max_length=100,choices=VITAMIN_CHOICES,null=True,
    blank=True,
    default=1)
    tr_ingredient = models.CharField(max_length=100)

class Advice(models.Model):
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    description = models.TextField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    