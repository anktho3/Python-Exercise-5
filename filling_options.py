import dict
import list
import vars

def filling_function(user_ingredient_selection):
    '''
        This function is used for filling selection. The user will make selections and any items they select will be added to the
        custOrder list and if there is a price associated with the item it will add the cost to add_ons and return that value.
    '''
    done = False
    add_ons = float(0)
    try:
        while done == False:
            # if user_ingredient_selection == str():
            #     print("Please only enter values 1 - 9.")

            if int(user_ingredient_selection) == 1:
                vars.custOrder.append(list.fillings_list[0])
                add_ons += dict.fillings_price["extra beans"]

            if int(user_ingredient_selection) == 2:
                vars.custOrder.append(list.fillings_list[1])
                add_ons += dict.fillings_price["chorizo"]

            if int(user_ingredient_selection) == 3:
                vars.custOrder.append(list.fillings_list[2])
                add_ons += dict.fillings_price["onions"]

            if int(user_ingredient_selection) == 4:
                vars.custOrder.append(list.fillings_list[3])
                add_ons += dict.fillings_price["peppers"]

            if int(user_ingredient_selection) == 5:
                vars.custOrder.append(list.fillings_list[4])
                add_ons += dict.fillings_price["salsa"]

            if int(user_ingredient_selection) == 6:
                vars.custOrder.append(list.fillings_list[5])
                add_ons += dict.fillings_price["green_chile_salsa"]

            if int(user_ingredient_selection) == 7:
                vars.custOrder.append(list.fillings_list[6])
                add_ons += dict.fillings_price["cheese"]

            if int(user_ingredient_selection) == 8:
                vars.custOrder.append(list.fillings_list[7])
                add_ons += dict.fillings_price["extra_cheese"]

            if int(user_ingredient_selection) == 9:
                vars.custOrder.append(list.fillings_list[8])
                add_ons += dict.fillings_price["potatoes"]
            # else:
            #     print("Sorry that option doesn't exist. Please make a selection 1 - 9.\n")

            print("Would you like to add any other fillings? [1 - 9] or No to finish your order. \n")
            user_ingredient_selection = input()
            try:
                if user_ingredient_selection[0].upper() == "N":
                    done = True
                    return add_ons
                else:
                    continue
            except ValueError:
                # done = True
                return add_ons
            except IndexError:
                done = True
                return add_ons
    except ValueError:
        return add_ons