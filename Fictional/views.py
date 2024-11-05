from django.shortcuts import render, redirect
from .models import Flavor, Ingredient, CustomerSuggestion
from .forms import SeasonalFlavorForm, IngredientForm, CustomerSuggestionForm

def home(request):
    return render(request, 'home.html')

def seasonal_flavors(request):
    flavors = Flavor.objects.all()
    return render(request, 'flavors.html', {'flavors': flavors})

def add_flavor(request):
    if request.method == 'POST':
        form = SeasonalFlavorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seasonal_flavors')
    else:
        form = SeasonalFlavorForm()
    return render(request, 'add_flavor.html', {'form': form})

def ingredient_inventory(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory.html', {'ingredients': ingredients})


def customer_suggestions(request):
    suggestions = CustomerSuggestion.objects.all()
    return render(request, 'suggestions.html', {'suggestions': suggestions})

def add_suggestion(request):
    if request.method == 'POST':
        form = CustomerSuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_suggestions')
    else:
        form = CustomerSuggestionForm()
    return render(request, 'add_suggestion.html', {'form': form})


