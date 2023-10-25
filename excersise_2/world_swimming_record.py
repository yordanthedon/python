import math

world_record_sec = float(input())
distance = float(input())
time_in_sec_m = float(input())

all_time_sec = distance * time_in_sec_m
delay = math.floor(distance / 15) * 12.5
total_time_with_delay = all_time_sec + delay

if world_record_sec <= total_time_with_delay:
    diff = total_time_with_delay - world_record_sec
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time_with_delay:.2f} seconds.")