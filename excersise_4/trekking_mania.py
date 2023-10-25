count_groups = int(input())

musala_sum = 0
monblan_sum = 0
kilimanjaro_sum = 0
k2_sum = 0
everest_sum = 0
total_sum = 0

for i in range(1, count_groups + 1):
    people = int(input())
    total_sum += people

    if people <= 5:
        musala_sum += people
    elif people <= 12:
        monblan_sum += people
    elif people <= 25:
        kilimanjaro_sum += people
    elif people <= 40:
        k2_sum += people
    elif people >= 41:
        everest_sum += people

percent_musala = musala_sum / total_sum * 100
print(f"{percent_musala:.2f}%")
percent_monblan = monblan_sum / total_sum * 100
print(f"{percent_monblan:.2f}%")
percent_kilimanjaro = kilimanjaro_sum / total_sum * 100
print(f"{percent_kilimanjaro:.2f}%")
percent_k2 = k2_sum / total_sum * 100
print(f"{percent_k2:.2f}%")
percent_everest = everest_sum / total_sum * 100
print(f"{percent_everest:.2f}%")
