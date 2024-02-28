from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import  PersonForm,AdvisorForm, ItemForm, ReportForm , Favorite_listForm
from .models import Person, Advisor, Item, Report, Favorite_list

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

def favorite_list(request):
    # favorite_items = Favorite_list.objects.all()
    current_user = request.session['username']
    if current_user is not None:
        current_person = Person.objects.get(name=current_user)
        
        favorite_items = Favorite_list.objects.filter(pr_name = current_person)
        item_details = []
        for favorite_item in favorite_items:
            # Construct the correct image URL
            image_url = favorite_item.item_id.image.url if favorite_item.item_id.image else ''
            # Remove the duplicate prefix '/item_images/item_images/'
            image_url = image_url.replace('/item_images/item_images/', '/item_images/')
            item_details.append({
                'pr_name': favorite_item.pr_name,
                'item_name': favorite_item.item_id.item_name,
                'category': favorite_item.item_id.get_category_display(),
                'calories': favorite_item.item_id.calories,
                'vitamin': favorite_item.item_id.get_vitamin_display(),
                'ingredient': favorite_item.item_id.ingredient,
                'image_url': image_url
            })
        return render(request, 'favorite_list.html', {'items': item_details})


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
    food_items_a = Item.objects.all()
    food_items = []
    for item in food_items_a:
        image_url = item.image.url if item.image else ''
        image_url = image_url.replace('/item_images/item_images/', '/item_images/')
        item_detail = {
            'item_name' : item.item_name,
            'category': item.get_category_display(),
            'calories': item.calories,
            'vitamin': item.get_vitamin_display(),
            'ingredient': item.ingredient,
            'image_url': image_url
        }
        food_items.append(item_detail)
    return render(r,'home.html',{'food_items': food_items})

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


def get_item_id_by_name(item_name):
    try:
        # Query the Item model to get the id of the item with the given name
        item = Item.objects.get(item_name=item_name)
        return item
    except Item.DoesNotExist:
        # Handle the case where the item with the given name does not exist
        return None
    
def get_peron_id_by_name(pr_name):
    try:
        # Query the Item model to get the id of the item with the given name
        pr = Person.objects.get(name=pr_name)
        return pr
    except Person.DoesNotExist:
        # Handle the case where the item with the given name does not exist
        return None

def add_to_favorites(request):
    if request.method == 'POST':
        # Get the ID of the food item from the POST data
        food_item_id = request.POST.get('food_item_id')
        # Get the currently logged-in user
        current_user = request.session['username']
        # Check if the user is authenticated and not an admin
        if current_user is not None:
            # Convert food_item_id to an Item instance
            item_id = get_item_id_by_name(food_item_id)
            pr_id = get_peron_id_by_name(current_user)
            # Check if the food item is not already in the favorites list
            if not Favorite_list.objects.filter(pr_name=pr_id, item_id=item_id).exists():
                favorite_item = Favorite_list(pr_name=pr_id, item_id=item_id)
                favorite_item.save()
    
    # Redirect back to the home page after adding the food item to favorites
    return redirect('home')