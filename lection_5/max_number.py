y = input()
max = -10000000000000
while y != "Stop":
    number = int(y)
    if number > max:
        max = number
    y = input()
print(max)