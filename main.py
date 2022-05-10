
base_price = float(5.00)
add_ons = float(0.00)  # Cost of add-ons will be added in this variable
total_price = float(0.00)
custOrder = []

def main_ingredients_function(user_ingredient_selection):
    '''
    This function is used for main ingredient selection. The user will make a selection and it will take the price of those items
    and return it.
    '''
    add_ons = float(0)
    done = False
    while done == False:
        if int(user_ingredient_selection) == 1:
            custOrder.append(main_ingredients[0])
            add_ons += main_ingredients_price["ground_beef"]

        if int(user_ingredient_selection) == 2:
            custOrder.append(main_ingredients[1])
            add_ons += main_ingredients_price["carne_asada"]

        if int(user_ingredient_selection) == 3:
            custOrder.append(main_ingredients[2])
            add_ons += main_ingredients_price["carne_adovada"]

        if int(user_ingredient_selection) == 4:
            custOrder.append(main_ingredients[3])
            add_ons += main_ingredients_price["scrambled_eggs"]

        if int(user_ingredient_selection) == 5:
            custOrder.append(main_ingredients[4])
            add_ons += main_ingredients_price["chicken"]

        if int(user_ingredient_selection) == 6:
            custOrder.append(main_ingredients[5])
            add_ons += main_ingredients_price["sofritas"]
        
        check = input("Would you like to make another protein selection? (it costs extra) [y/N] \n")
        try:
            if check[0].upper() == "Y":
                print("Please add another meat of your choice.")
                print("######## DOUBLE PROTEINS ########")
                for item_number, proteins in enumerate(double_meat):  # Prints out the items as a numbered list for main ingredients
                    print(item_number + 1, proteins.replace("_", " ").capitalize())
                print("##########################")
                user_ingredient_selection = input("Please select your protein using values 1 - 6: \n")
                add_ons += double_meat_function(user_ingredient_selection)
                return add_ons
            else:
                print("Understood, moving to next options for your order.\n")
                return add_ons
        except IndexError:
            print("Understood, moving to next options for your order.\n")
            return add_ons
        except ValueError:
            break

def double_meat_function(user_ingredient_selection):
    '''
    This function is used for mo'meat selection. The user will make a selection and it will take the price of those items
    and return it.
    '''
    add_ons = float(0)
    done = False
    while done == False:
        if int(user_ingredient_selection) == 1:
            custOrder.append(double_meat[0])
            add_ons += double_meat_price["double_ground_beef"]

        if int(user_ingredient_selection) == 2:
            custOrder.append(double_meat[1])
            add_ons += double_meat_price["double_carne_asada"]

        if int(user_ingredient_selection) == 3:
            custOrder.append(double_meat[2])
            add_ons += double_meat_price["double_carne_adovada"]

        if int(user_ingredient_selection) == 4:
            custOrder.append(double_meat[3])
            add_ons += double_meat_price["double_scrambled_eggs"]

        if int(user_ingredient_selection) == 5:
            custOrder.append(double_meat[4])
            add_ons += double_meat_price["double_chicken"]

        if int(user_ingredient_selection) == 6:
            custOrder.append(double_meat[5])
            add_ons += double_meat_price["double_sofritas"]
        
        check = input("Would you like to make another selection? [y/N] \n")
        try:
            if check[0].upper() == "Y":
                print("Please make another selection.")
            else:
                print("Understood, moving to next options for your order.\n")
                return add_ons
        except IndexError:
            print("Understood, moving to next options for your order.\n")
            return add_ons
        except ValueError:
            break




def rice_beans_function(user_ingredient_selection):
    '''
    This function is used for rice or bean selection. The user will make selections and any items they select will be added to the
    custOrder list and if there is a price associated with the item it will add the cost to add_ons and return that value.
    '''
    add_ons = float(0)
    done = False
    try:
        while done == False:
            if int(user_ingredient_selection) == 1:
                custOrder.append(rice_or_beans[0])
                add_ons += rice_or_beans_price["rice"]

            if int(user_ingredient_selection) == 2:
                custOrder.append(rice_or_beans[1])
                add_ons += rice_or_beans_price["cilantro_rice"]

            if int(user_ingredient_selection) == 3:
                custOrder.append(rice_or_beans[2])
                add_ons += rice_or_beans_price["beans"]

            if int(user_ingredient_selection) == 4:
                custOrder.append(rice_or_beans[3])
                add_ons += rice_or_beans_price["no_beans"]
            print("Would you like to add any other Rice or Beans? [1 - 4] or No to finish your order \n")
            user_ingredient_selection = input()
            try:
                if user_ingredient_selection[0].upper() == "N":
                    done = True
                    return add_ons
                else:
                    continue
            except ValueError:
                break
            except IndexError:
                done = True
                return add_ons
    except:
        return add_ons

def filling_function(user_ingredient_selection):
    '''
        This function is used for filling selection. The user will make selections and any items they select will be added to the
        custOrder list and if there is a price associated with the item it will add the cost to add_ons and return that value.
    '''
    done = False
    add_ons = float(0)
    try:
        while done == False:
            if user_ingredient_selection == str():
                print("Please only enter values 1 - 9.")

            if int(user_ingredient_selection) == 1:
                custOrder.append(fillings_list[0])
                add_ons += fillings_price["extra beans"]

            if int(user_ingredient_selection) == 2:
                custOrder.append(fillings_list[1])
                add_ons += fillings_price["chorizo"]

            if int(user_ingredient_selection) == 3:
                custOrder.append(fillings_list[2])
                add_ons += fillings_price["onions"]

            if int(user_ingredient_selection) == 4:
                custOrder.append(fillings_list[3])
                add_ons += fillings_price["peppers"]

            if int(user_ingredient_selection) == 5:
                custOrder.append(fillings_list[4])
                add_ons += fillings_price["salsa"]

            if int(user_ingredient_selection) == 6:
                custOrder.append(fillings_list[5])
                add_ons += fillings_price["green_chile_salsa"]

            if int(user_ingredient_selection) == 7:
                custOrder.append(fillings_list[6])
                add_ons += fillings_price["cheese"]

            if int(user_ingredient_selection) == 8:
                custOrder.append(fillings_list[7])
                add_ons += fillings_price["extra_cheese"]

            if int(user_ingredient_selection) == 9:
                custOrder.append(fillings_list[8])
                add_ons += fillings_price["potatoes"]
            # else:
            #     done = True
            #     return add_ons
            print("Would you like to add any other fillings? [1 - 9] or No to finish your order. \n")
            user_ingredient_selection = input()
            try:
                if user_ingredient_selection[0].upper() == "N":
                    done = True
                    return add_ons
                else:
                    continue
            except ValueError:
                done = True
                return add_ons
            except IndexError:
                done = True
                return add_ons
    except ValueError:
        print("Please only enter values 1 - 9.")

        
        


main_ingredients = [
    "ground_beef ($5.00)",
    "carne_asada ($6.00)", # Add $1
    "carne_adovada ($6.00)", # Add $1
    "scrambled_eggs ($5.00)",
    "chicken ($5.00)",
    "sofritas ($5.00)",
]

main_ingredients_price = {
    "ground_beef" : 0.00,
    "carne_asada" : 1.00, # Add $1
    "carne_adovada" : 1.00, # Add $1
    "scrambled_eggs" : 0.00,
    "chicken" : 0.00,
    "sofritas" : 0.00,
}

# Double meat prices for customers that want extra.
double_meat = [
    "ground_beef ($1.00)",
    "carne_asada ($2.00)", # Add $1
    "carne_adovada ($2.00)", # Add $1
    "scrambled_eggs ($1.00)",
    "chicken ($1.00)",
    "sofritas ($1.00)",
]

double_meat_price= {
    "double_ground_beef" : 1.00,
    "double_carne_asada" : 2.00, # Add $1
    "double_carne_adovada" : 2.00, # Add $1
    "double_scrambled_eggs" : 1.00,
    "double_chicken" : 1.00,
    "double_sofritas" : 1.00,
}


rice_or_beans = [
    "rice (add $0.25)", # Add $0.25
    "cilantro_rice (add $0.25)", # Add $ 0.25
    "beans",
    "no_beans",
]

rice_or_beans_price = {
    "rice" : 0.25, # Add $0.25
    "cilantro_rice" : 0.25, # Add $ 0.25
    "beans" : 0.00,
    "no_beans" : 0.00,
}

fillings_list = [
    "extra beans (add $.50)", # $0.50
    "chorizo (add $1.00)", # $1
    "onions",
    "peppers",
    "salsa",
    "green_chile_salsa (add $0.25", # Add $0.25
    "cheese",
    "extra_cheese (add $0.50)",  # Add $0.50
    "potatoes (add $0.50)", # Add $1
]

fillings_price = {
    "extra beans" : 0.50, # $0.50
    "chorizo" : 1.00, # Add $1
    "onions" : 0.00,
    "peppers" : 0.00,
    "salsa" : 0.00,
    "green_chile_salsa" : 0.25, # Add $0.25
    "cheese" : 0.00,
    "extra_cheese" : 0.50,  # Add $0.50
    "potatoes" : 1.00, # Add $1
}


'''
Main
'''

name = input("What is your name? ").title()
print("Hello " + name + ", Welcome to Neato Burrito!\n")

print("Please select the ingredients you would like in your Burrito below.\n")

print("######## PROTEINS ########")
for item_number, ingredients in enumerate(main_ingredients):  # Prints out the items as a numbered list for main ingredients
    print(item_number + 1, ingredients.replace("_", " ").capitalize())
print("##########################")
print("Please select your protein using values 1 - 6: \n")
try:
    user_ingredient_selection = input()
    add_ons += main_ingredients_function(user_ingredient_selection)
except ValueError:
    print("Standard burrito is beef, okay?")
    custOrder.append(main_ingredients[0])
    
print("You have selected:\n" + str(custOrder[:]))
print("")

print("######### RICE & BEANS #########")
for item_number, rice_beans in enumerate(rice_or_beans):  # Prints out the items as a numbered list for Rice and beans
    print(item_number + 1, rice_beans.replace("_", " ").capitalize())
print("################################")
print("Please select one of the Rice and Beans options using values 1 - 4: \n")
user_ingredient_selection = input()
add_ons += rice_beans_function(user_ingredient_selection)



print("You have selected:\n" + str(custOrder[:]))

print("Please select the fillings you would like to add to the burrito.\n")
print("######### FILLINGS #########")
for item_number, fillings in enumerate(fillings_list):  # Prints out the items as a numbered list
    print(item_number + 1, fillings.replace("_", " ").capitalize())
print("############################")
print("Please select your filling using values 1 - 9: \n")
user_ingredient_selection = input()
add_ons += filling_function(user_ingredient_selection)

# This calculates the total price of the order with addons.
total_price = base_price + add_ons

print("\n######## ORDER #########")
for items in custOrder:
    print(items.replace("_", " ").capitalize())
print("########################")
print("Total price: ${:.2f}".format(total_price)) # Using specific formatting to get 2 decimal point precision.

# print(add_ons)
print("\nPlease confirm your order by agreeing to the price and listed ingredients.\n")


# Loop asks customer for confirmation and will cancel order if not accepted
while True:
    try:
        order = input("Would you like to continue with your purchase? [y/N] \n")
        if order[0].upper() == "Y":
            print("Order confirmed.")
            break
        else:
            print("Order canceled")
            break
    except IndexError:
        print("Order canceled")
        break
print("Thank you for your purchase. Enjoy and have a great day!\n")
