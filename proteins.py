import dict
import list
import vars
import double_proteins

def main_ingredients_function(user_ingredient_selection):
    '''
    This function is used for main ingredient selection. The user will make a selection and it will take the price of those items
    and return it.
    '''
    add_ons = float(0)
    done = False
    while done == False:
        if int(user_ingredient_selection) == 1:
            vars.custOrder.append(list.main_ingredients[0])
            add_ons += dict.main_ingredients_price["ground_beef"]

        if int(user_ingredient_selection) == 2:
            vars.custOrder.append(list.main_ingredients[1])
            add_ons += dict.main_ingredients_price["carne_asada"]

        if int(user_ingredient_selection) == 3:
            vars.custOrder.append(list.main_ingredients[2])
            add_ons += dict.main_ingredients_price["carne_adovada"]

        if int(user_ingredient_selection) == 4:
            vars.custOrder.append(list.main_ingredients[3])
            add_ons += dict.main_ingredients_price["scrambled_eggs"]

        if int(user_ingredient_selection) == 5:
            vars.custOrder.append(list.main_ingredients[4])
            add_ons += dict.main_ingredients_price["chicken"]

        if int(user_ingredient_selection) == 6:
            vars.custOrder.append(list.main_ingredients[5])
            add_ons += dict.main_ingredients_price["sofritas"]
        # else:
        #     print("Sorry that option doesn't exist. Please make a selection 1 - 6.\n")
        #     continue
        
        check = input("Would you like to make another protein selection? (it costs extra) [y/N] \n")
        try:
            if check[0].upper() == "Y":
                print("Please add another meat of your choice.")
                print("######## DOUBLE PROTEINS ########")
                print("")
                for item_number, proteins in enumerate(list.double_meat):  # Prints out the items as a numbered list for main ingredients
                    print(item_number + 1, proteins.replace("_", " ").capitalize())
                print("")
                print("##########################")
                user_ingredient_selection = input("Please select your protein using values 1 - 6: \n")
                add_ons += double_proteins.double_meat_function(user_ingredient_selection)
                return add_ons
            else:
                print("Understood, moving to next options for your order.\n")
                return add_ons
        except IndexError:
            print("Understood, moving to next options for your order.\n")
            return add_ons
        except ValueError:
            break