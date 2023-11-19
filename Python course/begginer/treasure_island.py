print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
Welcome to the Treasure Island !
Your mission is to find the treasute.                                                                 
''')
left_right = input("The road splits to 'right' and 'left'. Which path do you take ?\n").lower()
if left_right != "left":
    print("You fell into a hole. Game over.")
else:
    swim_wait = input("You come across a river. Do you want to try to 'swim' across or do you 'wait' for a boat?\n").lower()
    if swim_wait != "wait":
        print("You have been attacked by trout. Game over.")
    else:
        red_blue_yellow = input("There are three doors in front of you, which one do you choose ? 'Red', 'blue' or 'yellow'?\n").lower()
        if red_blue_yellow == "red":
            print("You died by fire. Game over.")
        elif red_blue_yellow == "blue":
            print("You fell into the pit of snakes. Game over.")
        elif red_blue_yellow == "yellow":
            print("You found the treasure !!!")
        else:
            print("You died. Game over.")