from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import  PersonForm,AdvisorForm, ItemForm, ReportForm , Favorite_listForm,EatenForm,TargetForm
from .models import Person, Advisor, Item, Report, Favorite_list,Eaten,Target, Advice
from django.contrib import messages
from django.db.models import Sum,F
from django.utils import timezone

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

def home(r):
    if r.session.session_key is None:
        return redirect('Login')
    food_items_a = Item.objects.all()
    food_items = []
    for item in food_items_a:
        item_detail = {
            'item_name' : item.item_name,
            'category': item.get_category_display(),
            'calories': item.calories,
            'vitamin': item.get_vitamin_display(),
            'ingredient': item.ingredient,
            'image_url': item.image.url
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
                return redirect('home2')
            
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
                messages.success(request, 'Item added to favorites successfully.')
            else:
                messages.error(request, 'Item is already in favorites.')
        else:
            messages.error(request, 'You must be logged in to add items to favorites.')
    # Redirect back to the home page after adding the food item to favorites
    return redirect('home')

def remove_from_favorites(request):
    if request.method == 'POST':
        # Get the ID of the food item from the POST data
        food_item_id = request.POST.get('food_item_id')
        current_user = request.session['username']

        if current_user is not None:
            item_id = get_item_id_by_name(food_item_id)
            pr_id = get_peron_id_by_name(current_user)
            favorite_item = Favorite_list.objects.filter(pr_name=pr_id, item_id=item_id).first()
            if favorite_item:
                favorite_item.delete()
                messages.success(request, 'Item removed from favorites successfully.')
            else:
                messages.error(request, 'Item not found in favorites.')
        else:
            messages.error(request, 'You must be logged in to remove items from favorites.')
    return redirect('favorite_list')

def mark_as_eaten(request):
    if request.method == 'POST':
        food_item_id = request.POST.get('food_item_id')
        quantity = request.POST.get('quantity', 1)
        current_user = request.session['username']
        if current_user is not None:
            try:
                item_id = get_item_id_by_name(food_item_id)
                pr_id = get_peron_id_by_name(current_user)
                # Create and save the Eaten instance
                eaten_item = Eaten.objects.filter(pr_name=pr_id, item_id=item_id).first()
                if eaten_item:
                    # If already eaten, update the quantity
                    eaten_item.quntity += int(quantity)
                    eaten_item.save()
                    messages.success(request, f'{quantity} item(s) added to the existing eaten items.')
                else:
                    # If not eaten yet, create a new Eaten instance
                    eaten_item = Eaten(pr_name=pr_id, item_id=item_id, quntity=quantity)
                    eaten_item.save()
                    messages.success(request, f'{quantity} item(s) marked as eaten.')
            except Person.DoesNotExist:
                messages.error(request, 'User does not exist.')
            except Item.DoesNotExist:
                messages.error(request, 'Item does not exist.')
        else:
            messages.error(request, 'You must be logged in to mark items as eaten.')

    return redirect('home')

def report_list(request):
    try:
        # Retrieve the person object
        current_user = request.session['username']
        person = Person.objects.get(name=current_user)
        
        # Query the eaten items for the person
        eaten_items = Eaten.objects.filter(pr_name=person)
        
        # Calculate total calories
        total_calories = eaten_items.aggregate(total_calories=Sum(F('item_id__calories') * F('quntity')))['total_calories'] or 0
        
        # Prepare consumed items list and total ingredients
        consumed_items = [f"{item.item_id.item_name} ({item.quntity})" for item in eaten_items]
        total_ingredients = list(set([item.item_id.ingredient for item in eaten_items]))
        total_vitamins = list(set([item.item_id.vitamin for item in eaten_items]))

        existing_report = Report.objects.filter(pr_nm=person, date=timezone.now().date()).first()
        if existing_report:
            # Update the existing report
            existing_report.total_calories = total_calories
            existing_report.total_vitamins = total_vitamins
            existing_report.consumed_items = ', '.join(consumed_items)
            existing_report.total_ingredient = ', '.join(total_ingredients)
            existing_report.save()
            messages.success(request, "Your report has been updated.")
            return redirect('home')
        # Create and save the report instance
        report = Report.objects.create(
            pr_nm=person,
            date=timezone.now(),
            total_calories=total_calories,
            total_vitamins=total_vitamins,
            consumed_items=', '.join(consumed_items),
            total_ingredient=', '.join(total_ingredients)
        )
        return redirect('report_lists')
    except Person.DoesNotExist:
        # Handle the case where the person with the given ID does not exist
        return redirect('home')
    
def report_lists(request):
    try:
        # Retrieve the current user
        current_user = request.session['username']
        person = Person.objects.get(name=current_user)
        
        # Query reports for the logged-in user
        reports = Report.objects.filter(pr_nm=person)
        
        return render(request, 'report_lists.html', {'reports': reports})
    except Person.DoesNotExist:
        # Handle the case where the person with the given ID does not exist
        return redirect('home')
    
def set_target(request):
    vitamin_choices = Target.VITAMIN_CHOICES
    if request.method == 'POST':
        current_user = request.session['username']
        tr_calories = request.POST['tr_calories']
        tr_vitamins = request.POST.getlist('tr_vitamins')  # Use getlist to retrieve multiple selected values
        tr_ingredient = request.POST['tr_ingredient']
        person = Person.objects.get(name=current_user)
        # You don't need to check form.is_valid() because you're not using a form here

        target = Target.objects.create(
            pr_nm=person,
            tr_calories=tr_calories,
            tr_vitamins=tr_vitamins,
            tr_ingredient=tr_ingredient
        )
        # Redirect to a success page or homepage
        return redirect('home')
    else:
        form = TargetForm()
    return render(request, 'set_target.html', {'form': form, 'VITAMIN_CHOICES': vitamin_choices})

def home2(request):
    if request.session.session_key is None:
        return redirect('Login')
    item_data = Item.objects.prefetch_related('advice_set').all()
    data={
        'item_data' : item_data,
    }
    return render(request,"home2.html",data)

def give_advice(request):
    if request.method == 'POST':
        advice_id = request.POST['advice_id']
        description = request.POST['description']
        advice_data = Advice.objects.get(id = advice_id)
        advice_data.description = description
        advice_data.save()
    return redirect(home2)

def delete_advice(request):
    if request.method == 'POST':
        advice_id = request.POST['advice_id']
        advice_data = Advice.objects.get(id = advice_id)
        advice_data.delete()
    return redirect(home2)

def add_advice(request):
    if request.method == 'POST':
        description = request.POST['description']
        item_id = request.POST['item_id']
        advi= Advisor.objects.get(name = request.session['username'])
        ite = Item.objects.get(id=item_id)
        new_advice = Advice(advisor=advi,description=description,item=ite)
        new_advice.save()
    return redirect(home2)
