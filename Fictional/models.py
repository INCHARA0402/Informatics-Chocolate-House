from django.db import models

class Flavor(models.Model):
    flavor_name = models.CharField(max_length=100)
    description = models.TextField()
    available_from = models.DateField()
    available_until = models.DateField()

    def _str_(self):
        return self.flavor_name

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=100)
    quantity_in_stock = models.PositiveIntegerField()
    unit = models.CharField(max_length=10)  # e.g., kg, L

    def _str_(self):
        return self.ingredient_name

class CustomerSuggestion(models.Model):
    customer_name = models.CharField(max_length=100)
    flavor_suggestion = models.CharField(max_length=100)
    allergy_concern = models.CharField(max_length=100, blank=True, null=True)

    def _str_(self):
        return f"{self.customer_name} - {self.flavor_suggestion}"
