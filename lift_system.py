current_floor = 0
while True :
    floor = int(input("enter floor to go: "))
    if(current_floor > floor):
         print("lift down for going to floor",floor)
    elif(current_floor < floor):
        print("lift up for going to floor",floor)
    elif(current_floor == floor):
        print("you are already in this floor")
    else:
        print("unknown floor number")

    
    current_floor = floor
    print("the current floor is",current_floor)
    print("open door")
