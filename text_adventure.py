import time
import sys
#this makes the presentation look nice
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
#creating the rooms
room=[[],["arrow"],["guard","arrow"],[],["blade"],[],["cross"],["hilt"],["throne","crown"],["grindstone"],["helmet"],["arrow"],["crafting_table","bow"]]
r=["a","Entrance to the Castle of  Richard Duke of Normandy","garrison quarters","hallway","war room","hallway","church","hallway","throne room","armoury","hallway","hallway","workshop"]

#basic movement
def go_north(current_room):
    if current_room==1 or current_room==2 or current_room==3 or current_room==4:   
        print_slow("Sorry.But you can not go further north!")
        return 0
    else:
        return -4
def go_south(current_room):
    if current_room==9 or current_room==10 or current_room==11 or current_room==12:
        print_slow("Sorry.But you can not go further south!")
        return 0
    else:
        return 4
def go_east(current_room):
    if current_room==4 or current_room==8 or current_room==12:
        print_slow("Sorry.But you can not go further east!")
        return 0
    else:
        return 1

def go_west(current_room):
    if current_room==1 or current_room==5 or current_room==9:
        print_slow("Sorry.But you  can not go further west!")

    else:
        return -1
#description of the room
def lookroom(i):
    
    if i==1:
        print_slow("You are at the :")
        print_slow(r[1])
        print_slow("The castle looks abandoned and the gate is open. After a close inspection  of the entrance it looks like this castle was attacked.")
        print_slow("We can say that the inhabitants left the castle during the attack and when the attackers entered the castle, they looted as much as they can and left if to rot.")
        print_slow("Possible exits: East, South")
        print_slow("Here you can see:")
        print_slow(room[1])
    elif i==2:
        print_slow("You are in the: ")
        print_slow(r[2])
        print_slow("This is the place where the soldiers spent their days when they were not on patrol. Here they ate, trained and waited until it was their turn to go on patrol. ")
        print_slow("Possible exits: West, East, South")
        print_slow("In this room you can see:")
        print_slow(room[2])
    elif i==3:
        print_slow("You are in the: ")
        print_slow(r[3])
        print_slow("A simple hallway")
        print_slow("Possible exits: West, East, South")
        print_slow("In this room you can see:")
        print_slow(room[3])
    elif i==4:
        print_slow("You are in the: ")
        print_slow(r[4])
        print_slow("This is the place where Richard and his generals discuss their next move, both politically and military")
        print_slow("Possible exits: West, South")
        print_slow("In this room you can see:")
        print_slow(room[4])
    elif i==5:
        print_slow("You are in the:")
        print_slow(r[5])
        print_slow("Simple hallway")
        print_slow("Possible exits: North, East, South")
        print_slow("In this room you can see:")
        print_slow(room[5])
    elif i==6:
        print_slow("You are in the: ")
        print_slow(r[6])
        print_slow("This church is small in size, but it had a n important role for the locals back then. Here they found wisdom,spiritual and mental conform and peace.")
        print_slow("Possible exits: North, West, East, South")
        print_slow("In this room you can see:")
        print_slow(room[6])
    elif i==7:
        print_slow("You are in the ")
        print_slow(r[7])
        print_slow("Simple hallway")
        print_slow("Possible exits: North, West, East, South")
        print_slow("In this room you can see:")
        print_slow(room[7])
    elif i==8:
        print_slow("You are in the ")
        print_slow(r[8])
        print_slow("Here you can find the throne of Richard. The is made out of marble and it is still intact.")
        print_slow("Possible exits: North, West, South")
        print_slow("In this room you can see:")
        print_slow(room[8])
    elif i==9:
        print_slow("You are in the ")
        print_slow(r[9])
        print_slow("This is the place where the soldiers stored their weapons and armour")
        print_slow("Possible exits: North,East")
        print_slow("In this room you can see:")
        print_slow(room[9])
    elif i==10:
        print_slow("You are in the ")
        print_slow(r[10])
        print_slow("Simple hallway")
        print_slow("Possible exits: North, West, East")
        print_slow("In this room you can see:")
        print_slow(room[10])
    elif i==11:
        print_slow("You are in the ")
        print_slow(r[11])
        print_slow("Simple hallway")
        print_slow("Possible exits: North, West, East")
        print_slow("In this room you can see:")
        print_slow(room[11])
    elif i==12:
        print_slow("You are in the ")
        print_slow(r[12])   
        print_slow("The castle was well-known back then because of its workshop, where products of high quality were made, including steel, glass and pottery.")
        print_slow("Possible exits: North, West")
        print_slow("In this room you can see:")
        print_slow(room[12])

#take item
def take(thing,i,room,inventory):
   
    if thing=="throne" or thing=="crafting_table" or thing=="grindstone" :
        print_slow("You can not carry that. It is too heavy")
    elif thing not in room[i]:
        print("It is not in the current room")
    else:
        room[i].remove(thing)
        inventory.append(thing)
        print_slow("Item is now in your inventory")
        
#use item
def use(thing,i,inventory):
    print_slow("Ok")
    if i==9 and thing=="grindstone" and "sword" in inventory:
        inventory.remove("sword")
        inventory.append("sharp_sword")
        print_slow("Now you are ready to kill the dragon. Run to the exit and save the kingdom, Knight.")
    else:
        if i==12 and thing=="crafting_table" and "blade" in inventory and "guard" in inventory and "hilt" in inventory:
            inventory.remove("blade")
            inventory.remove("hilt")
            inventory.remove("guard")
            inventory.append("sword")
            print_slow("You made the Ascalon, the legendary sword of Saint George. Now find a grindstone to make it sharp enough to kill the dragon")
#drop item
def drop(thing,i,room,inventory):
    inventory.remove(thing)
    room[i].append(thing)
    print_slow("Ok")
    
#look item  
def look(thing,i,inventory,room):
    if thing not in inventory and  thing not in room[i]:
         print_slow("That item is not in your inventory,nor in the current room")
    else:
        print("a")
        if thing=="blade":
             print_slow("Blade of the Ascalon,made out of Damascus Steel and forged in Rome. You can feel the power of God in it. It is blunt at the moment.")
        elif thing =="guard":
             print_slow("Guard of the Ascalon, with beautiful engravings on it.If you look closer, you can see the image of Christ, the cross and the acvila. After all, it is aint George's sword and it was made in Rome.")
        elif thing=="hilt":
             print_slow("Hilt of the Ascalon.It is made made out of olive wood with straps made out of lion leather")
        elif thing=="cross":
             print_slow("A golden cross made in the tenth century")
        elif thing=="crown":
             print_slow("Crown of Richard Duke of Normandy, made out of gold, silver and decorated with precious gems")
        elif thing== "arrow":
             print_slow("Simple arrow")
        elif thing=="helmet":
             print_slow("Rusty helmet")
        else:
             print_slow("Simple bow")
#commands
def commands():
    print_slow("'go north' gets you in northen room")
    print_slow("'go south' gets you in the southern room")
    print_slow("'go east' gets you in the eastern room")
    print_slow("'go west' gets you in the western room ")
    print_slow("'look room' gets you a list of items in your current room and a description of the room")
    print_slow("'look <item>' gets you a short description of an item which is in your inventory")
    print_slow("'drop <item>' drop a certain item which is in your inventory ")
    print_slow("'use <item>' uses a specific item in your inventory")
    print_slow("'take <item>' will take an item from current room and will put in in your inventory")
#small talk to introduce the player to the game
def intro():
    print_slow("Greetings, Knight!")
    print_slow("My name is Sir Denis Remo Ban of Severin.")
    print_slow("I will guide you while you search in this castle for the Ascalon,used by Saint George to slay the dragon, the same dragon that is now raveging the realm. ")
    print_slow("As I was told, your mission is to slay the dragon, as Saint George once did in the legend.")
    print_slow("And there is no better weapon than the sword that slayed the dragon.")
    name=input("What is your name,Knight? ")
    title=input("What is your title, if you have such thing?")
    print_slow("So, you are searching for the Ascalon in this castle,the Castle of Richard Duke of Normandy.")
    print_slow("The sword is broken into 3 pieces: the blade, the hilt and the guard.")
    print_slow("After you collect all of them, you have to use a crafting table to make the sword.")
    print_slow("After that you have to find a grindstone to sharp the blade.Once the blade is sharp, run to the exit and save the realm.")
    print_slow("Good luck, Knight!")
    print_slow("If you need help, enter <help> and I will show the commands")
intro()
current_room=1
inventory=[]
#main loop
while True:
    print_slow("Enter your command,Knight")
    command=input()
    if command=="go north":
        current_room += go_north(current_room)
    elif command=="go south":
        current_room += go_south(current_room)
    elif command=="go west":
       current_room +=  go_west(current_room) 
    elif command=="go east":
       current_room +=  go_east(current_room)
    elif command=="help":
        commands()
    elif command=="lookroom":
        lookroom(current_room)
    else:
         splitList=command.split(" ")
         if splitList[0]=='use':
             use(splitList[1],current_room,inventory)
         elif splitList[0]=='look':
             if splitList[1]=='room':
                 lookroom(current_room)
             else:
                 look(splitList[1],current_room,inventory,room)
         elif splitList[0]=='drop':
             drop(splitList[1],current_room,room,inventory)
         elif splitList[0]=='take':
             take(splitList[1],current_room,room,inventory)
    if current_room==1 and "sharp_sword" in inventory:
        print("You have the Ascalon. Now get out there and get rid of the dragon once and for all, like Saint George once did." )
        print("THE END")
        break


