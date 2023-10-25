days = int(input())
room = input()
grade = input()

nights = days - 1
total_cost = 0
if room == "room for one person":
    if days < 10:
        nights *= 18
        total_cost = nights
    elif 10 <= days <= 15:
        nights *= 18
        total_cost = nights
    elif 15 < days:
        nights *= 18
        total_cost = nights
elif room == "apartment":
    if days < 10:
        nights *= 25
        total_cost = nights * 0.7
    elif 10 <= days <= 15:
        nights *= 25
        total_cost = nights * 0.65
    elif 15 < days:
        nights *= 25
        total_cost = nights * 0.5

elif room == "president apartment":
    if days < 10:
        nights *= 35
        total_cost = nights * 0.90
    elif 10 <= days <= 15:
        nights *= 35
        total_cost = nights * 0.85
    elif 15 < days:
        nights *= 35
        total_cost = nights * 0.80

if grade == "positive":
    total_cost = total_cost * 1.25
else:
    total_cost = total_cost * 0.9
print(f"{total_cost:.2f}")