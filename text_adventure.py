#creating the rooms
room[1]=[]
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
room[8]=["throne","crown"]
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
    time.sleep(1)
    if current_room==1 or current_room==2 or current_room==3 or current_room==4:
        print("Sorry.But you can not go further north!")
    else:
        current_room=current_room-4
def go_south(current_room):
    time.sleep(1)
    if current_room==9 or current_room==10 or current_room==11 or current_room==12:
        print("Sorry.But you can not go further south!")
    else:
          current_room=current_room+4
def go_east(current_room):
    time.sleep(1)
    if current_room==4 or current_room==8 or current_room==12:
        print("Sorry,Sir.But you can not go further east!")
    else:
            current_room+=1

def go_west(current_room):
    time.sleep(1)
    if current_room==1 or current_room==5 or current_room==9:
        print("Sorry.But you noy can go further west!")
    else:
        current_room-=1
#description of the room
def look(i):
    time.sleep(1)
    i=current_room
    print("You are in the ")
    print(r[i])
    print("In this room you can see:")
    print(room[i])
#take item
def take(thing,i):
    if thing=throne or thing=crafting_table or thing=grindstone:
        print("You can carry that. It is too heavy")
    else:
        inventory.append(thing)
        room[i].remove(thing)
#use item
def use(thing,i):
    if i==9 and thing="grindstone" and "sword" in inventory:
        time.sleep(1)
        inventory.remove("sword")
        inventory.append("sharp_sword")
        print("Now you are ready to kill the dragon. Run to the exit and save the kingdom, Knight.")
        else:
            if i==12 and thing="crafting_table" and "blade" in inventory and "guard" in inventory and "hilt" in inventory:
                time.sleep(1)
                inventory.remove("blade")
                inventory.remove("hilt")
                inventory.remove("guard")
                inventory.append("sword")
                print("You made the Ascalon, the legendary sword of Saint George. Now find a grindstone to make it sharp enough to kill the dragon")
#drop item
def drop(thing,i):
    inventory.remove(thing)
    room[i].append(thing)
#look item 
def look(thing):
    time.sleep(1)
    if thing in inventory:
        if thing=blade:
            print("Blade of the Ascalon,made out of Damascus Steel and forged in Rome. You can feel the power of God in it. It is blunt at the moment.")
        else:
            if thing =guard:
                print("Guard of the Ascalon, with beautiful engravings on it.If you look closer, you can see the image of Christ, the cross and the acvila. After all, it is aint George's sword and it was made in Rome.")
            else:
                if thing=hilt:
                    print("Hilt of the Ascalon.It is made made out of olive wood with straps made out of lion leather")
                else:
                    if thing=cross:
                        print("A goden cross made in the tenth century")
                    else:
                        if thing=crown:
                            print("Crown of Richard Duke of Normandy,made out of gold, silver and decorated with precious gems")
                        else:
                            if thing= arrow:
                                print("Simple arrow")
                            else:
                                if thing=helmet:
                                    print("Rusty helmet")
                                else:
                                    print("Simple bow")
    else:
        print("That item is not in your inventory")
def intro():
    print("Greetings, Knight!")
    time.sleep(1)
    print("My name is Sir Denis of Severin.I will guide you while you search in this catle for the Ascalon, used by Saint George to slay the dragon, the same dragon that is now raveging the realm. ")
    time.sleep(1)
    name=input("What is your name,Knight? ")
    time.sleep(1)
    print("So, you are searching for the Ascalon in this catle,the Castle of  Richard Duke of Normandy.")
    time.sleep(1)
    print("The sword is broken into 3 pieces: the blade, the hilt and the guard. After you collect all of them, you have to use a crafting table to make the sword.")
    time.sleep(1)
    print("After that you have to find a grindstone to sharp the blade.Once the blade is sharp, run to the exit and save the realm.")
    time.sleep(1)
    print("Good luck, Knight!")
