fruit = input()
day = input()
quen = float(input())
price = 0
flag = True
if day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == "orange":
        price = 0.9
    elif fruit == "grapefruit":
        price = 1.6
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        flag = False
elif day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == "banana":
        price = 2.5
    elif fruit == 'apple':
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    else:
        flag = False
else:
    flag = False
if flag:
    print(f"{(price * quen):.2f}")
else:
    print("error")