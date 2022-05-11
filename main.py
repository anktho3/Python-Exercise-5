'''
This application is designed to be used as ordering software for Neato Burrito. It will greet a customer and start the ordering
process. The customer will then be able to confirm their order or cancel it.
'''
import proteins
import ricebeansMod
import filling_options
import vars
import list

######## 
# Main #
########

# Get customer name and greet them
name = input("What is your name? ").title()
print("Hello " + name + ", Welcome to Neato Burrito!\n")

print("Please select the ingredients you would like in your Burrito below.\n")

# Protein selection
print("######## PROTEINS ########")
print("")
for item_number, ingredients in enumerate(list.main_ingredients):  # Prints out the items as a numbered list for main ingredients
    print(item_number + 1, ingredients.replace("_", " ").capitalize())
print("")
print("##########################")
print("Please select your protein using values 1 - 6: \n")
# While loop for protein selection. The try/except blocks are configured for error handling.
while True:
    user_ingredient_selection = input()
    try:
        if len(user_ingredient_selection) == 0:
            print("Standard burrito is beef.")
            vars.custOrder.append(list.main_ingredients[0])         
        elif int(user_ingredient_selection) < 1 or int(user_ingredient_selection) > 6:
            raise ValueError
        break
    except ValueError:
        print("Sorry that option doesn't exist. Please make a selection 1 - 6.\n")
        continue
    except IndexError:
        print("Sorry that option doesn't exist. Please make a selection 1 - 6.\n")
        continue
# try/except block for adding rice and beans cost to add_ons variable
try:
    vars.add_ons += proteins.main_ingredients_function(user_ingredient_selection)
except ValueError:
    print("")

print("You have selected:\n" + str(vars.custOrder[:]))
print("")

# Rice and Bean selection
print("######### RICE & BEANS #########")
print("")
for item_number, rice_beans in enumerate(list.rice_or_beans):  # Prints out the items as a numbered list for Rice and beans
    print(item_number + 1, rice_beans.replace("_", " ").capitalize())
print("")
print("################################")
print("Please select one of the Rice and Beans options using values 1 - 4: \n")
# While loop for the rice and beans selection. The try/except blocks are configured for error handling.
# user_ingredient_selection = input()

while True:
    user_ingredient_selection = input()
    try:
        if len(user_ingredient_selection) == 0:
            print("Standard selection is No Rice or Beans.")    
        elif int(user_ingredient_selection) < 1 or int(user_ingredient_selection) > 4:
            raise ValueError
        break
    except ValueError:
        print("Sorry that option doesn't exist. Please make a selection 1 - 4.\n")
        continue
    except IndexError:
        print("Sorry that option doesn't exist. Please make a selection 1 - 4.\n")
        continue
# try/except block for adding rice and beans cost to add_ons variable
try:
    vars.add_ons += ricebeansMod.rice_beans_function(user_ingredient_selection)
except ValueError:
    print("")

print("You have selected:\n" + str(vars.custOrder[:]))

# Fillings selection
print("Please select the fillings you would like to add to the burrito.\n")
print("######### FILLINGS #########")
print("")
for item_number, filling_items in enumerate(list.fillings_list):  # Prints out the items as a numbered list
    print(item_number + 1, filling_items.replace("_", " ").capitalize())
print("")
print("############################")
print("Please select your filling using values 1 - 9: \n")
# While loop for filling selection. The try/except blocks are configured for error handling.
while True:
    user_ingredient_selection = input()
    try:
        if len(user_ingredient_selection) == 0:
            print("Standard burrito has no fillings")       
        elif int(user_ingredient_selection) < 1 or int(user_ingredient_selection) > 9:
            raise ValueError
        break
    except ValueError:
        print("Sorry that option doesn't exist. Please make a selection 1 - 9.\n")
        continue
    except IndexError:
        print("Sorry that option doesn't exist. Please make a selection 1 - 9.\n")
        continue
# try/except block for adding filling cost to add_ons variable
try:
    vars.add_ons += filling_options.filling_function(user_ingredient_selection)
except ValueError:
    print("")

# This calculates the total price of the order with addons.
vars.total_price = vars.base_price + vars.add_ons

# Prints out order for confirmation
print("\n######## ORDER #########")
print("")
for items in vars.custOrder:
    print(items.replace("_", " ").capitalize())
print("")
print("########################")
print("Total price: ${:.2f}".format(vars.total_price)) # Using specific formatting to get 2 decimal point precision.

# print(add_ons)
print("\nPlease confirm your order by agreeing to the price and listed ingredients.\n")

# Loop asks customer for confirmation and will cancel order if not accepted
while True:
    try:
        order = input("Would you like to continue with your purchase? [y/N]: ")
        if order[0].upper() == "Y":
            print("\nOrder confirmed.")
            print("\nThank you for your purchase. Enjoy and have a great day!\n")
            break
        else:
            print("\nOrder canceled")
            print("\nHave a great day!")
            break
    except IndexError:
        print("\nOrder canceled")
        print("\nHave a great day!")
        break

## End ##