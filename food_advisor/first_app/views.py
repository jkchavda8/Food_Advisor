from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import  PersonForm,AdvisorForm, ItemForm, ReportForm
from .models import Person, Advisor, Item, Report

def create_person(request):
    if request.method == 'POST':
        nm = request.POST['name']
        p=Person.objects.filter(name=nm)
        if len(p) == 1:
            message = "username is already exist"
            return render(request,'create_person.html',{'message':message})
        if request.POST['password']!=request.POST['cpassword']:
            message = "confirm password not match"
            return render(request,'create_person.html',{'message':message})
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['username'] = nm
            return redirect('home')  # Redirect to person list page after successful creation
    else:
        form = PersonForm()
    return render(request, 'create_person.html', {'form': form})

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'persons': persons})

def create_advisor(request):
    if request.method == 'POST':
        nm = request.POST['name']
        p=Advisor.objects.filter(name=nm)
        if len(p) == 1:
            message = "username is already exist"
            return render(request,'create_person.html',{'message':message})
        if request.POST['password']!=request.POST['cpassword']:
            message = "confirm password not match"
            return render(request,'create_person.html',{'message':message})
        if request.POST['password']!=request.POST['cpassword']:
            return redirect('create_advisor')
        form = AdvisorForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['username'] = nm
            return redirect('home')  # Redirect to advisor list page after successful creation
    else:
        form = AdvisorForm()
    return render(request, 'create_advisor.html', {'form': form})

def advisor_list(request):
    advisors = Advisor.objects.all()
    return render(request, 'advisor_list.html', {'advisors': advisors})

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to item list page after successful creation
    else:
        form = ItemForm()
    return render(request, 'create_item.html', {'form': form})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_list')  # Redirect to report list page after successful creation
    else:
        form = ReportForm()
    return render(request, 'create_report.html', {'form': form})

def report_list(request):
    reports = Report.objects.all()
    return render(request, 'report_list.html', {'reports': reports})

def home(r):
    if r.session.session_key is None:
        return redirect('Login')
    return render(r,'home.html')

def Login(r):
    if r.method=='POST':
        if r.POST['usertype']=='user':
            user=r.POST['username']
            password=r.POST['password']
            p=Person.objects.filter(name=user,password=password).values()
            if len(p)==1:
                r.session['username'] = user
                return redirect('home')
        elif r.POST['usertype']=='advisor':
            user=r.POST['username']
            password=r.POST['password']
            p=Advisor.objects.filter(name=user,password=password).values()
            if len(p) == 1:
                r.session['username'] = user
                return redirect('home')
            
        else:
            return redirect('Login')

    return render(r,'Login.html')

def Logout(r):
    r.session.flush()
    return redirect('Login')
