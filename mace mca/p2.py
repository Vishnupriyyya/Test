l=list(map(int,input("Enter list:").split(' ')))
num= int(input("Enter element to search:"))

first,last=0,len(l)-1
Found =False

while first<=last:
    mid = (first + last)//2
    if l[mid]==num:
        print("Element Found")
        Found = True
        break
    elif l[mid]<num:
        first = mid + 1
    else:
        last = mid - 1
if not Found:
    print("Not Found")




  
