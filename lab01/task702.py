def train_sort(shedule):
    
    for i in range(len(shedule)-1):
        flag = False 
        for j in range(len(shedule) - i - 1):
            if shedule[j][0] > shedule[j + 1][0]:
                shedule[j], shedule[j + 1] = shedule[j + 1], shedule[j]
                flag = True
            elif (shedule[j][0] == shedule[j + 1][0]) and (shedule[j][2] < shedule[j + 1][2]):
                shedule[j], shedule[j + 1] = shedule[j + 1], shedule[j]
                flag = True
        if not flag:
            break

    for k in range(len(shedule)):
        print(f"{shedule[k][0]} will departure for {shedule[k][1]} at {shedule[k][2]}")
 
train_numbers = int(input())
train_list = []
 
for i in range(train_numbers):
    info = input().split()
    name = info[0]
    destination = info[4]
    departure_time = info[6]
    train_list.append([name, destination, departure_time])
 
train_sort(train_list)
