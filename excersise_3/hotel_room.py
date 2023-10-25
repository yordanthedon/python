month = input()
nights = int(input())
studio_price = 0
apartament_price = 0

if month == "May" or month == "October":
    studio_price = nights * 50
    apartament_price = nights * 65
elif month == "June" or month == "September":
    studio_price = nights * 75.20
    apartament_price = nights * 68.70
elif month == "July" or month == "August":
    studio_price = nights * 76
    apartament_price = nights * 77

if nights > 14 and (month == "May" or month == "October"):
    studio_price = studio_price * 0.70
elif nights > 7 and (month == "May" or month == "October"):
    studio_price = studio_price * 0.95
elif nights > 14 and (month == "June" or month == "September"):
    studio_price = studio_price * 0.8

if nights > 14:
    apartament_price = apartament_price * 0.9

print(f"Apartment: {apartament_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")