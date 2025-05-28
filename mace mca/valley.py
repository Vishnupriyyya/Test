steps=input("Enter input:")
level=0
valley=0

for i in steps:
    if i == "U":
        level += 1
    elif i ==  "D":
        level -= 1
    else:
        print("Invalid input")
        break
    if level == 0 and i == "U":
        valley += 1
print(valley)
