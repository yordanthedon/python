import math

days_off = int(input())
food = int(input())
first_deer = float(input())
second_deer = float(input())
third_deer = float(input())

deer_one = days_off * first_deer
deer_two = days_off * second_deer
deer_three = days_off * third_deer

total_food = deer_one + deer_two + deer_three
diff = abs(food - total_food)
if total_food <= food:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")