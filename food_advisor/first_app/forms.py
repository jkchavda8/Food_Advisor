# forms.py
from django import forms
from .models import Person, Advisor, Item, Report,Favorite_list

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'email', 'gender', 'phone_no','password']

class AdvisorForm(forms.ModelForm):
    class Meta:
        model = Advisor
        fields = ['name', 'email', 'specification','password']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'category', 'calories', 'vitamin', 'ingredient','image']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['pr_nm','date', 'total_calories', 'quentity']

class Favorite_listForm(forms.ModelForm):
    class Meta:
        model = Favorite_list
        fields = ['pr_name','item_id']