n = int(input())

current_number = 1
current_bigger_than_n = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        if current_number > n:
            current_bigger_than_n = True
            break
        print(str(current_number) + ' ', end='')
        current_number += 1
    if current_bigger_than_n:
        break
    print()