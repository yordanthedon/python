price_processor = float(input())
price_videocard = float(input())
price_ram = float(input())
count_ram = int(input())
discount = float(input())

price_processor_leva = price_processor * 1.57
price_videocard_leva = price_videocard * 1.57
price_ram_leva = price_ram * 1.57
total_ram = price_ram_leva * count_ram

price_processor_leva = price_processor_leva - (price_processor_leva * discount)
price_videocard_leva = price_videocard_leva - (price_videocard_leva * discount)

total_cost = total_ram + price_videocard_leva + price_processor_leva
print(f"Money needed - {total_cost:.2f} leva.")