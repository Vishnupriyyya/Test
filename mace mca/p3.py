n=input("enter:")
count=0
for i in n:
    if i=="{":
        count+=1
    elif i=="}":
        count-=1
    else:
        print("Invalid Character")
    if count < 0:
        print("not valid")
        break
if count==0:
    print("Valid")
else:
    print("Not matching")