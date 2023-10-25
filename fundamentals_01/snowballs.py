import math

number_of_snowbawlls = int(input())
max_value = 0
max_snowball_weight = 0
max_snowball_time = 0
max_snowball_quality = 0

for snowball in range(number_of_snowbawlls):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = math.pow(snowball_weight / snowball_time, snowball_quality)
    if value > max_value:
        max_value = value
        max_snowball_weight = snowball_weight
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality
print(f"{max_snowball_weight} : {max_snowball_time} = {int(max_value)} ({max_snowball_quality})")