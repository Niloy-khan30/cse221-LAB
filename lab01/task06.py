
def sort(n, student_ids, student_marks):
    swaps = 0
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if (student_marks[j] > student_marks[max_idx]) or (student_marks[j] == student_marks[max_idx] and student_ids[j] < student_ids[max_idx]):
                max_idx = j
        
        if max_idx != i:
            student_ids[i], student_ids[max_idx] = student_ids[max_idx], student_ids[i]
            student_marks[i], student_marks[max_idx] = student_marks[max_idx], student_marks[i]
            swaps += 1
    
    print(f'Minimum swaps: {swaps}')
    for i in range(n):
        print(f"ID: {student_ids[i]} Mark: {student_marks[i]}")


n = int(input())
student_ids = list(map(int, input().split()))
student_marks =  list(map(int, input().split()))

sort(n, student_ids, student_marks)



        

    
# n = 7
# id = [7,4,9,3,2,5,1]
# mark = [40, 50, 50, 20, 10, 10, 10]
    
# sort(n,id, mark)