from pyscript import document  # webpage module links
# your roll_dice function should be saved in a file named 'dice.py'
# uncomment the next line when you have this prepared
import dice
import random

# GLOBAL (script-wide) variable
# this stores the selected face option from the drop-down list
dice_type = "2-sided", "4-sided", "6-sided", "8-sided", 
"10-sided", "20-sided", "100-sided",


def select_face_option(event):
    global dice_type  # use global var named dice_type
    ...  # replace with your own code

    dice_type = int(event.target.value)

def roll_all_dice(event):
    global dice_type  # use global var named dice_type
    ...  # replace with your own code

    document.querySelector("div#roll-history").innerHTML = "<p id='something'> + str()>"

def clear_history(event):
    # this finds the div tag with id attribute 'roll-history' and clears whatever is inside
    document.querySelector("div#roll-history").innerHTML = ""