n = int(input())

liters = 0
total_degree_liter = 0
degrees = 0
for i in range(n):

    q_rakia = float(input())
    liters += q_rakia
    g_rakia = float(input())
    total_degree_liter += q_rakia * g_rakia
degrees = total_degree_liter / liters

print(f"Liter: {liters:.2f}")
print(f"Degrees: {degrees:.2f}")
if degrees < 38:
    print("Not good, you should baking!")
elif 38 <= degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")