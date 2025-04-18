def calculate():
    n = int(input())
    for i in range(n):
        x = input().split(' ')
        if x[2] == '+':
            print(int(x[1]) + int(x[3]))
        elif x[2] == '-':
            print(int(x[1]) - int(x[3]))
        elif x[2] == '*':
            print(int(x[1]) * int(x[3]))
        else:
            print(int(x[1]) / int(x[3]))

calculate()