
Fictional Chocolate House:

This is a Django-based web application designed for a fictional chocolate house. The application uses an SQLite database to manage:

Seasonal Flavor Offerings: Track seasonal chocolate flavors and their availability dates.
Ingredient Inventory: Keep track of available ingredients and their quantities.
Customer Flavor Suggestions: Receive customer flavor suggestions along with any allergy concerns.

Features

1. View and Add Seasonal Flavors: 
   - View a list of available seasonal flavors, their descriptions, and availability dates.
   - Add new seasonal flavors with a description, and specify start and end availability dates.

2. View Ingredient Inventory:
   - View the ingredient inventory with available quantities and units.

3. Customer Suggestions with Allergy Concerns:
   - View customer suggestions for new flavors along with any allergy-related concerns.
   - Add new customer suggestions.


Installation and Setup

## Prerequisites

- Python 3.6+
- pip (Python package installer)

## Steps

1. Clone the Repository

   Clone the project repository to your local machine.

   bash
   git clone https://github.com/yourusername/chocolate-house.git
   cd chocolate-house
   
   

2. Set Up the Database

   Django uses SQLite by default. Run the following commands to create the database and apply migrations.

   bash
   python manage.py makemigrations
   python manage.py migrate
   

3. Create a Superuser (Optional)

   To access the Django admin interface, create a superuser account.

   bash
   python manage.py createsuperuser
   

4. Run the Development Server

   Start the Django development server.

   bash
   python manage.py runserver
   

5. Access the Application

   Open your web browser and visit http://127.0.0.1:8000/ to view the application.


## Application Structure

The project is structured as follows:

- Chocolates: The main project folder.
  - Fictional: The main app that includes views, models, forms, and templates.
  - templates: HTML templates for displaying data and forms.
  - models.py: Contains the data models for Seasonal Flavors, Ingredients, and Customer Suggestions.
  - views.py: Contains the logic for handling requests and rendering responses.
  - forms.py: Contains form classes for user input.



## Models

Flavor

- Fields:
  - flavor_name: Name of the flavor (e.g., "Pumpkin Spice").
  - description: Description of the flavor.
  - available_from: Date when the flavor becomes available.
  - available_until: Date until which the flavor will be available.

Ingredient

- Fields:
  - ingredient_name: Name of the ingredient (e.g., "Cocoa").
  - quantity_in_stock: Quantity in stock.
  - unit: Unit of measurement (e.g., "kg", "L").

CustomerSuggestion

- Fields:
  - customer_name: Name of the customer submitting the suggestion.
  - flavor_suggestion: Suggested flavor.
  - allergy_concern: Any allergy concerns related to the suggestion.



## Usage

- Home Page: Links to view seasonal flavors, ingredient inventory, and customer suggestions.

- Seasonal Flavors:
  - View available seasonal flavors.
  - Add new flavors with a name, description, and availability dates.

- Ingredient Inventory:
  - View ingredient quantities in the inventory.
  
- Customer Suggestions:
  - View customer suggestions for new flavors and related allergy concerns.
  - Add new customer suggestions.

---

## Admin Interface

To manage data using Django's admin interface, navigate to http://127.0.0.1:8000/admin. You’ll need to log in with your superuser credentials.

In the admin interface, you can:
- Add, update, or delete entries for Seasonal Flavors, Ingredients, and Customer Suggestions.



## Acknowledgments

- Built with Django, an open-source web framework.


This README.md file provides an overview of the application, installation steps, and usage details.