budget = float(input())
season = input()

destination = ""
place = ""
expensive = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        expensive = budget * 0.3
    else:
        place = "Hotel"
        expensive = budget * 0.7

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        expensive = budget * 0.4
    else:
        place = "Hotel"
        expensive = budget * 0.8

elif budget >= 1000:
    destination = "Europe"
    place = "Hotel"
    expensive = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {expensive:.2f}")