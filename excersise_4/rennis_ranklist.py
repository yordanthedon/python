import math

tournaments = int(input())
init_points = int(input())

win_count = 0
points = init_points

for i in range(1, tournaments + 1):
    finished = input()
    if finished == "W":
        win_count += 1
        points += 2000
    elif finished == "F":
        points += 1200
    elif finished == "SF":
        points += 720

print(f"Final points: {points}")
points_without_int = points - init_points
average_pts = math.floor(points_without_int/ tournaments)
print(f"Average points: {average_pts}")
win_percent = win_count / tournaments * 100
print(f"{win_percent:.2f}%")