import time
#creating the rooms
room[1]=["arrow"]
r[1]="Entrance to the Castle of  Richard Duke of Normandy"
room[2]=["guard","arrow"]
r[2]="garrison quarters"
room[3]=[]
r[3]="hallway"
room[4]=["blade"]
r[4]="war room"
room[5]=[]
r[5]="hallway"
room[6]=["cross"]
r[6]="pray room"
room[7]=["hilt"]
r[7]="hallway"
room[7]=["throne","crown"]
r[8]="throne room"
room[9]=["grindstone"]
r[9]="armoury"
room[10]=["helmet"]
r[10]="hallway"
room[11]=["arrow"]
r[11]="hallway"
room[12]=["crafting_table","bow"]
r[12]="workshop"
#basic movement
def go_north(current_room):
    time.sleep(3)
    if current_room==1 or current_room==2 or current_room==3 or current_room==4:
        print("Sorry.But you can not go further north!")
    else:
        current_room=current_room-4
def go_south(current_room):
    time.sleep(3)
    if current_room==9 or current_room==10 or current_room==11 or current_room==12:
        print("Sorry.But you can not go further south!")
    else:
          current_room=current_room+4
def go_east(current_room):
    time.sleep(3)
    if current_room==4 or current_room==8 or current_room==12:
        print("Sorry,Sir.But you can not go further east!")
    else:
            current_room+=1

def go_west(current_room):
    time.sleep(3)
    if current_room==1 or current_room==5 or current_room==9:
        print("Sorry.But you noy can go further west!")
    else:
        current_room-=1

#description of the room
def lookroom(i):
    time.sleep(3)
    
    if i==1:
        print("You are at the :")
        print(r[1])
        print("The castle looks abandoned and the gate is open. After a close inspection  of the entrance it looks like this castke was attacked.")
        print("We can say that the inhabitants left the castle during the attack and when the attackers entered the castle, they looted as much as they can and left if to rot.")
        print("Here you can see:")
        print(room[1])
    else:
        if i==2:
            print("You are in the: ")
            print(r[2])
            print()
            print("In this room you can see:")
            print(room[2])
        else:
            if i==3:
                print("You are in the: ")
                print(r[3])
                print()
                print("In this room you can see:")
                print(room[3])
            else:
                if i==4:
                    print("You are in the: ")
                    print(r[4])
                    print()
                    print("In this room you can see:")
                    print(room[4])
                else:
                    if i==5:
                        print("You are in the:")
                        print(r[5])
                        print()
                        print("In this room you can see:")
                        print(room[5])
                    else:
                        if i==6:
                            print("You are in the: ")
                            print(r[6])
                            print()
                            print("In this room you can see:")
                            print(room[6])
                        else:
                            if i==7:
                                print("You are in the ")
                                print(r[7])
                                print()
                                print("In this room you can see:")
                                print(room[7])
                            else:
                                if i==8:
                                    print("You are in the ")
                                    print(r[8])
                                    print()
                                    print("In this room you can see:")
                                    print(room[8])
                                else:
                                    if i==9:
                                        print("You are in the ")
                                        print(r[9])
                                        print()
                                        print("In this room you can see:")
                                        print(room[9])
                                    else:
                                        if i==10:
                                            print("You are in the ")
                                            print(r[10])
                                            print()
                                            print("In this room you can see:")
                                            print(room[10])
                                        else:
                                            if i==11:
                                                print("You are in the ")
                                                print(r[11])
                                                print()
                                                print("In this room you can see:")
                                                print(room[11])
                                            else:
                                                if i==12:
                                                    print("You are in the ")
                                                    print(r[12])
                                                    print()
                                                    print("In this room you can see:")
                                                    print(room[12])

#take item
def take(thing,i):
    time.sleep(3)
    print("Item is now in your inventory")
    if thing=="throne" or thing=="crafting_table" or thing=="grindstone":
        print("You can not carry that. It is too heavy")
    else:
        inventory.append(thing)
        room[i].remove(thing)
#use item
def use(thing,i):
    print("Ok")
    time.sleep(3)
    if i==9 and thing=="grindstone" and "sword" in inventory:
        time.sleep(1)
        inventory.remove("sword")
        inventory.append("sharp_sword")
        print("Now you are ready to kill the dragon. Run to the exit and save the kingdom, Knight.")
    else:
        if i==12 and thing=="crafting_table" and "blade" in inventory and "guard" in inventory and "hilt" in inventory:
            time.sleep(3)
            inventory.remove("blade")
            inventory.remove("hilt")
            inventory.remove("guard")
            inventory.append("sword")
            print("You made the Ascalon, the legendary sword of Saint George. Now find a grindstone to make it sharp enough to kill the dragon")
#drop item
def drop(thing,i):
    time.sleep(3)
    inventory.remove(thing)
    room[i].append(thing)
    print("Ok")
    
#look item  
def look(thing,i):
    time.sleep(3)
    if thing not in inventory or thing not in room[i]:
         print("That item can not be found either in your inventory nor in the current room")
    else:
        if thing=="blade":
             print("Blade of the Ascalon,made out of Damascus Steel and forged in Rome. You can feel the power of God in it. It is blunt at the moment.")
        elif thing =="guard":
             print("Guard of the Ascalon, with beautiful engravings on it.If you look closer, you can see the image of Christ, the cross and the acvila. After all, it is aint George's sword and it was made in Rome.")
        elif thing=="hilt":
             print("Hilt of the Ascalon.It is made made out of olive wood with straps made out of lion leather")
        elif thing=="cross":
             print("A goden cross made in the tenth century")
        elif thing=="crown":
             print("Crown of Richard Duke of Normandy,made out of gold, silver and decorated with precious gems")
        elif thing== "arrow":
             print("Simple arrow")
        elif thing=="helmet":
             print("Rusty helmet")
        else:
             print("Simple bow")
#commands
def commands():
    time.sleep(3)
    print("'go north' gets you in northen room")
    print("'go south' gets you in the southern room")
    print("'go east' gets you in the eastern room")
    print("'go west' gets you in the western room ")
    print("'lookroom' gets you a list of items in your current room and a description of the room")
    print("'look <item>' gets you a short description of an item which is in your inventory or in the current room")
    print("'drop <item>' drop a certain item which is in your inventory ")
    print("'use <item>' uses a specific item, in this case the grindstone or the crafting table")
    print("'take <item>' will take an item from current room and will put in in your inventory")
#small talk to introduce the player to the game
def intro():
    print("Greetings, Knight!")
    time.sleep(3)
    print("My name is Sir Denis Remo Ban of Severin.")
    time.sleep(3)
    print("I will guide you while you search in this catle for the Ascalon,used by Saint George to slay the dragon, the same dragon that is now raveging the realm. ")
    time.sleep(3)
    print("As I was told, your mission is to slay the dragon, as Saint George once did in the legend.")
    time.sleep(3)
    print("And there is no better weapon than the sword that slayed the dragon.")
    time.sleep(3)
    name=input("What is your name,Knight? ")
    time.sleep(3)
    title=input(print("What is your title, if you have such thing?"))
    time.sleep(3)
    print("So, you are searching for the Ascalon in this castle,the Castle of Richard Duke of Normandy.")
    time.sleep(3)
    print("The sword is broken into 3 pieces: the blade, the hilt and the guard.")
    time.sleep(3)
    print("After you collect all of them, you have to use a crafting table to make the sword.")
    time.sleep(3)
    print("After that you have to find a grindstone to sharp the blade.Once the blade is sharp, run to the exit and save the realm.")
    time.sleep(3)
    print("Good luck, Knight!")
    time.sleep(3)
    print("If you need help, enter <help> and I will show the commands")
intro()
current_room=1
#main loop
while True:
    command=input(print("Enter your command,Knight"))
    if command=="go north":
        go_north()
    elif command=="go south":
        go_south()
    elif command=="go west":
        go_west() 
    elif command=="go east":
        go_east()
    elif command=="help":
        commands()
    elif command=="lookroom":
        lookroom(current_room)


