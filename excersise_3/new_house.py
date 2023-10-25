flowers = input()
c_flowers = int(input())
buget = int(input())
t_sum = 0
if flowers == "Roses":
    t_sum = c_flowers * 5
    if c_flowers > 80:
        t_sum = t_sum * 0.9
elif flowers == "Dahlias":
    t_sum = c_flowers * 3.8
    if c_flowers > 90:
        t_sum =t_sum * 0.85
elif flowers == "Tulips":
    t_sum = c_flowers * 2.80
    if c_flowers > 80:
        t_sum = t_sum * 0.85
elif flowers == "Narcissus":
    t_sum = c_flowers * 3
    if c_flowers < 120:
        t_sum = t_sum * 1.15
elif flowers == "Gladiolus":
    t_sum = c_flowers * 2.50
    if c_flowers < 80:
        t_sum = t_sum * 1.20

diff = abs(buget - t_sum)
if buget >= t_sum:
    print(f"Hey, you have a great garden with {c_flowers} {flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")