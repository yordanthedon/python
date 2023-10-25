buget = float(input())
videocards = int(input())
processors = int(input())
ram = int(input())
price_video = 250
total_video = videocards * 250
price_processor = total_video * 0.35
total_proc = processors * price_processor
price_ram = total_video * 0.1
total_ram = ram * price_ram
total_sum = total_ram + total_proc + total_video
if processors < videocards:
    total_sum = total_sum - total_sum * 0.15
diff = abs(buget - total_sum)
if total_sum <= buget:
    print(f"You have {diff:.2f} leva left!")
if total_sum > buget:
    print(f"Not enough money! You need {diff:.2f} leva more!")