def evenORodd():
    n = int(input())
    for i in range(n):
        num = int(input('enter the number : '))
        if num % 2 == 0 :
            print(f'{num} is an Even number.')
        else:
            print(f'{num} is an Odd number.')

evenORodd()