import math

first = int(input())
second = int(input())
third = int(input())
total = first + second +third
min = total // 60
sec = total % 60
min = math.floor(min)
if sec < 10:
    print(f'{min}:0{sec}')
else:
    print(f'{min}:{sec}')