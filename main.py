

name = input("What is your name?").title()
print("Hello " + name + ", Welcome to Neato Burrito!\n")


main_ingredients = [
    "ground_beef",
    "carne_asada", # Add $1
    "carne_adovada", # Add $1
    "scrambled_eggs",
    "chicken",
    "sofritas",
]



main_ingredients_price = {
    "ground_beef" : 0.00,
    "carne_asada" : 1.00, # Add $1
    "carne_adovada" : 1.00, # Add $1
    "scrambled_eggs" : 0.00,
    "chicken" : 0.00,
    "sofritas" : 0.00,
}

rice_or_beans = [
    "rice", # Add $0.25
    "cilantro_rice", # Add $ 0.25
    "beans",
    "no_beans",
]

rice_or_beans_price = {
    "rice" : 0.25, # Add $0.25
    "cilantro_rice" : 0.25, # Add $ 0.25
    "beans" : 0.00,
    "no_beans" : 0.00,
}

fillings = [
    "extra beans", # $0.50
    "chorizo", # $1
    "onion",
    "peppers",
    "salsa",
    "green_chile_salsa", # Add $0.25
    "cheese",
    "extra_cheese",  # Add $0.50
    "potatoes", # Add $1
]

fillings_price = {
    "extra beans" : 0.50, # $0.50
    "chorizo" : 1.00, # Add $1
    "onion" : 0.00,
    "peppers" : 0.00,
    "salsa" : 0.00,
    "green_chile_salsa" : 0.25, # Add $0.25
    "cheese" : 0.00,
    "extra_cheese" : 0.50,  # Add $0.50
    "potatoes" : 1.00, # Add $1
}

base_price = float(5)
add_ons = float(0)  # Cost of add-ons will be added in this variable
total_price = float()
 

print("Please select the ingredients you would like in your Burrito below.\n")
for index, ingredients in enumerate(main_ingredients_price):
    print(index, ingredients.replace("_", " ").capitalize())

user_ingredient_selection = input()

#if main_ingredients[0] == user_ingredient_selection:
    
print(main_ingredients_price['carne_asada'])

