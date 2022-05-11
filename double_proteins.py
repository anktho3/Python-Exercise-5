import dict
import list
import vars

def double_meat_function(user_ingredient_selection):
    '''
    This function is used for mo'meat selection. The user will make a selection and it will take the price of those items
    and return it.
    '''
    add_ons = float(0)
    done = False
    while done == False:
        if int(user_ingredient_selection) == 1:
            vars.custOrder.append(list.double_meat[0])
            add_ons += dict.double_meat_price["double_ground_beef"]

        if int(user_ingredient_selection) == 2:
            vars.custOrder.append(list.double_meat[1])
            add_ons += dict.double_meat_price["double_carne_asada"]

        if int(user_ingredient_selection) == 3:
            vars.custOrder.append(list.double_meat[2])
            add_ons += dict.double_meat_price["double_carne_adovada"]

        if int(user_ingredient_selection) == 4:
            vars.custOrder.append(list.double_meat[3])
            add_ons += dict.double_meat_price["double_scrambled_eggs"]

        if int(user_ingredient_selection) == 5:
            vars.custOrder.append(list.double_meat[4])
            add_ons += dict.double_meat_price["double_chicken"]

        if int(user_ingredient_selection) == 6:
            vars.custOrder.append(list.double_meat[5])
            add_ons += dict.double_meat_price["double_sofritas"]
        # else:
        #     print("Sorry that option doesn't exist. Please make a selection 1 - 6\n")

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
