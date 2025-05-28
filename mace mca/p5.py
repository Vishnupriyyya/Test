n=12
q=[[1,5,3],[4,8,7],[6,9,1],[8,10,9]]
Array = [0]*(n+1)

for start, end, value in q:
    Array[start] +=value
    Array[end] -=value
for i in range(1, n+1):
        Array[i] +=Array[i-1]
print(Array)
print(max(Array))
