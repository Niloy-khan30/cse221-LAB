def bubbleSort():
    n = int(input())
    arr = input().split()  
    a = list(map(int, arr))                                                 
    for i in range(n-1):
        flag = False
        for j in range(n-i-1): 
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = True
        if flag == False :
            break
    for x in range(n):
        if x == len(a)-1:
            print(a[x])
        else:
            print(a[x], end = ' ')


bubbleSort()