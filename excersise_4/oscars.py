actor_name = input()
academy_points = float(input())
n = int(input())

total_p = academy_points

for i in range(1, n + 1):
    name = input()
    points = float(input())

    c_points = (len(name) * points) / 2
    total_p += c_points

    if total_p >= 1250.5:
        break

if total_p < 1250.5:
    diff = 1250.5 - total_p
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_p:.1f}!")