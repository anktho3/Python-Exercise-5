import dict
import list
import vars

def rice_beans_function(user_ingredient_selection):
    '''
    This function is used for rice or bean selection. The user will make selections and any items they select will be added to the
    custOrder list and if there is a price associated with the item it will add the cost to add_ons and return that value.
    '''
    add_ons = float(0)
    done = False
    while done == False:
        try:
            if int(user_ingredient_selection) == 1:
                vars.custOrder.append(list.rice_or_beans[0])
                add_ons += dict.rice_or_beans_price["rice"]

            if int(user_ingredient_selection) == 2:
                vars.custOrder.append(list.rice_or_beans[1])
                add_ons += dict.rice_or_beans_price["cilantro_rice"]

            if int(user_ingredient_selection) == 3:
                vars.custOrder.append(list.rice_or_beans[2])
                add_ons += dict.rice_or_beans_price["beans"]

            if int(user_ingredient_selection) == 4:
                vars.custOrder.append(list.rice_or_beans[3])
                add_ons += dict.rice_or_beans_price["no_beans"]
            # else:
            #     print("Sorry that option doesn't exist. Please make a selection 1 - 4.\n")

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