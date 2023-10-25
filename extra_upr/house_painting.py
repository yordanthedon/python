x = float(input())
y = float(input())
h = float(input())
zadna = x * x
predna = zadna - 1.2 * 2
zadna_predna = zadna + predna
prozorec = 1.5 * 1.5
strana = (x * y) - prozorec
strani = strana + strana
green = zadna_predna + strani
green_b = green / 3.4
r_side = x * y
r_sides = r_side + r_side
r_front = x * h / 2
r_fronts = r_front + r_front
roof = r_sides + r_fronts
red_b = roof / 4.3
print(f"{green_b: .2f}")
print(f"{red_b: .2f}")