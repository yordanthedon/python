budget = float(input())
count_statists = int(input())
price_clothing_one = float(input())

decor_price = budget * 0.1
all_clothes_sum = count_statists * price_clothing_one

if count_statists > 150:
    all_clothes_sum = all_clothes_sum * 0.9

total_sum = decor_price + all_clothes_sum

diff = abs(budget - total_sum)
if budget >= total_sum:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")