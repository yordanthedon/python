deposit = float(input())
month = int(input())
glp = float(input())
lihva = deposit * glp / 100
lihva_mesec = lihva / 12
total = deposit + month * lihva_mesec
print(total)