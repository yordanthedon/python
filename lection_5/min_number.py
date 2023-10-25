y = input()
mini = 10000000000000
while y != "Stop":
    number = int(y)
    if number < mini:
        mini = number
    y = input()
print(mini)