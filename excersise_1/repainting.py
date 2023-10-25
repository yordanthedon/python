nailon = float(input())
boq = float(input())
amb = float(input())
hours_work = float(input())
p_nailon = 1.50
p_boq = 14.50
p_amb = 5.00
trb = 0.40
sum_nailon = (nailon + 2) * p_nailon
sum_boq = (boq*1.1) * p_boq
sum_amb = amb * p_amb
total_tools = sum_nailon + sum_boq + sum_amb + trb
workers = (total_tools * 0.3) * hours_work
total = total_tools + workers
print(total)
