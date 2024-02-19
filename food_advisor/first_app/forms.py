# forms.py
from django import forms
from .models import Person, Advisor, Item, Report

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
        fields = ['item_name', 'category', 'calories', 'vitamin', 'ingredient']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['date', 'total_calories', 'quentity']
