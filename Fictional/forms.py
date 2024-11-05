from django import forms
from Fictional.models import Ingredient, CustomerSuggestion, Flavor

class SeasonalFlavorForm(forms.ModelForm):
    class Meta:
        model = Flavor
        fields = ['flavor_name', 'description', 'available_from', 'available_until']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient_name', 'quantity_in_stock', 'unit']

class CustomerSuggestionForm(forms.ModelForm):
    class Meta:
        model = CustomerSuggestion
        fields = ['customer_name', 'flavor_suggestion', 'allergy_concern']