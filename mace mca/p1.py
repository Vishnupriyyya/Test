inputArr= list(map(int,input("Enter list:").rstrip().split(' ')))

minArr= float('inf')
maxArr=-float('inf')

for i in inputArr:
    if minArr >i:
        minArr = i
    if maxArr < i:
        maxArr = i

print(minArr,maxArr)