budget = int(input())
season = input()
fishmen = int(input())
t_cost = 0
if season == "Spring":
    if fishmen <= 6:
        t_cost = 3000 * 0.9
    if 7 <= fishmen <= 11:
        t_cost = 3000 * 0.85
    if fishmen >= 12:
        t_cost = 3000 * 0.75
elif season == "Summer":
    if fishmen <= 6:
        t_cost = 4200 * 0.9
    if 7 <= fishmen <= 11:
        t_cost = 4200 * 0.85
    if fishmen >= 12:
        t_cost = 4200 * 0.75
elif season == "Autumn":
    if fishmen <= 6:
        t_cost = 4200 * 0.9
    if 7 <= fishmen <= 11:
        t_cost = 4200 * 0.85
    if fishmen >= 12:
        t_cost = 4200 * 0.75
elif season == "Winter":
    if fishmen <= 6:
        t_cost = 2600 * 0.9
    if 7 <= fishmen <= 11:
        t_cost = 2600 * 0.85
    if fishmen >= 12:
        t_cost = 2600 * 0.75

if fishmen % 2 == 0 and season != "Autumn":
    t_cost = t_cost * 0.95

diff = abs(budget - t_cost)
if budget >= t_cost:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")