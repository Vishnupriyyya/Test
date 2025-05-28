def arrayManipulation(queries, n): 
    A = [0] * (n + 1) 
    for start, end, value in queries: 
        A[start-1] += value 
        A[end] -= value 
    max_val = 0 
    running_sum = 0 
    for num in A: 
        running_sum += num 
        max_val = max(max_val, running_sum) 
    return max_val
n=int(input("Enter limit:"))
queries = [[1, 5, 3], [4, 8, 7],[6,9,1],[8,13,5]]
print(arrayManipulation(queries, n))  