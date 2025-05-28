def pyramid(rows):
    k = 0
    for i in range(1, rows + 1):
        for space in range(1, (rows - i) + 1):
            print(end="  ")
        while k != (2 * i - 1):
            print("* ", end="")
            k += 1
        k = 0
        print()


test_cases = int(input())

for t in range(test_cases):
    rows = int(input())
    pyramid(rows)
