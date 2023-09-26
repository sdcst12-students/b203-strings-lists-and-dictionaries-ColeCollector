#!python3
"""
##### Task 5
create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they choose to 'get item', add that item to their inventory.  If they choose to drop item' remove that item from that invenory.  If they choose 'show inventory' give them a list of the items that they have.

Possible extensions:
* nicer format for displaying inventory
* use shortened/abbreviated names for items (recognizing first few characters or spelling errors)

possible items:
food
water
rope
torch
sack
wood
iron
steel
ginger
garlic
fish
stone
wool

example:
>get food
>get water
>get water
>get iron
>get 3 wood
>inventory
You have:
 1 food
 2 water
 1 iron
 3 wood
 >
"""


inv = {}
items = {"food" : "fod", "water": "war", "rope" : "roe", "torch" : "tor", "sack" : "sak", "wood" : "wod", "iron": "irn","steel" : "stl","ginger" : "gir","garlic": "gac","fish" : " fih","stone" : "ste","wool" : "wol"}

while True:
    action = input(">")
    action = action.split(" ")
    if action[0] == "get":
        if action[-1] in items:
            if len(action)== 3:
                if items[action[2]] in inv:
                    inv[items[action[2]]]+= int(action[1])
                else:
                    inv[items[action[2]]] = int(action[1])
            else:
                if items[action[1]] in inv:
                    inv[items[action[1]]] += 1
                else:
                    inv[items[action[1]]] = 1
        else:
            print("That's not an item")

    elif action[0] == "drop":
        if action[-1] in items:
            for i in inv:
                if i == items[action[-1]]:
                    if inv[items[action[1]]] == 0:
                        print("You can't do that")

                    else:
                        inv[items[action[1]]]= (inv[items[action[1]]]) - 1
                    break
        else:
            print("That's not an item")

    elif action[0] == "inventory":
        print("You have:\n")
        for i in inv:
            for j in items:
                if items[j] == i:
                    if inv[i] != 0:
                        print(inv[i],j)