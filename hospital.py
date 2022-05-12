hospital_rooms = {'Normal room':'1 flat bed + 2 normal masks','Oxygen room':'2 oxygen cylinders + 1 recliner bed + 2 non-rebreather masks','ICU':'1 ventilator + 1 recliner bed + 1 oxygen cylinder'}
rooms = {'Normal room':50,'Oxygen room':50,'ICU':20}
n=int(input('Enter the number of patients : '))
for i in range(n):
    print(f"Patient {i+1}")
    print()
    for x in hospital_rooms:
        print(x + ' : ' + hospital_rooms[x])
    print()
    room=input("Please enter the type of room you want to reserve : ")
    for key in rooms:
        if rooms[key] <= 50 or rooms[key] <= 20:
            for x in hospital_rooms:
                if x == room:
                    print('01 ' + x + ' (' + hospital_rooms[x] + ') reserved.')
            rooms[room]-=1
            print("Remaining availability : ")
            for x in rooms:
                print(x + ' : ' + str(rooms[x]))
            print()
            break
        else:
            print('Sorry, no rooms could be reserved.')
    