def array_reverse():
    inp1 = input().split(' ')
    arr = input().split(' ')

    for i in range(int(inp1[1])-1,-1,-1):

        if i == 0 :
            print(arr[i])
        else:
            print(arr[i], end= ' ')

array_reverse()

    




