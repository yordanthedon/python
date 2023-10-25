days = int(input())
room = input()
assesment = input()
nights = days - 1
expenses = 0

if room == "room for one person":
    expenses = 18 * nights
elif room == "apartment":
    expenses = 25 * nights
    if days < 10:
        expenses = expenses * 0.7
    elif 10 <= days <= 15:
        expenses = expenses * 0.85
    else:
        expenses = expenses * 0.5
elif room == "president apartment":
    expenses = 35 * nights
    if days < 10:
        expenses = expenses * 0.9
    elif 10 <= days <= 15:
        expenses = expenses * 0.85
    else:
        expenses = expenses * 0.8
if assesment == "positive":
    expenses = expenses * 1.25
else:
    expenses = expenses * 0.90
print(f"{expenses:.2f}")