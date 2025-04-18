def Bubble_Sort(my_lst):
    i = 0
    while True:
        flag = False
        j = 0 
        while j < (len(my_lst) - i - 1):
            if my_lst[j][0] > my_lst[j + 1][0]:
                my_lst[j], my_lst[j + 1] = my_lst[j + 1], my_lst[j]
                flag = True
            elif (my_lst[j][0] == my_lst[j + 1][0]) and (my_lst[j][2] < my_lst[j + 1][2]):
                my_lst[j], my_lst[j + 1] = my_lst[j + 1], my_lst[j]
                flag = True
            j += 1
        if not flag:
            break
        i += 1
    return my_lst
 
train_numbers = int(input())
train_list = []
 
for i in range(train_numbers):
    train_info = input().split()
    train_name = train_info[0]
    destination = train_info[4]
    departure_time = train_info[6]
    train_list.append([train_name, destination, departure_time])
 
sorted_train_list = Bubble_Sort(train_list)
for k in range(len(sorted_train_list)):
    print(f"{sorted_train_list[k][0]} will departure for {sorted_train_list[k][1]} at {sorted_train_list[k][2]}")