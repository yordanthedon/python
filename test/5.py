cel_za_denq = int(input())
barber = input()

oborot = 0
while barber != "closed":
    if  barber == "haircut":
        barber = input()
        if barber == "mens":
            oborot += 15
        elif barber == "ladies":
            oborot += 20
        elif barber == "kids":
            oborot += 10
    elif barber == "color":
        barber = input()
        if barber == "touch up":
            oborot += 20
        elif barber== "full color":
            oborot += 30

    if cel_za_denq <= oborot:
        print(f"You have reached your target for the day!")
        break
    barber = input()
diff = abs(oborot - cel_za_denq)
if cel_za_denq > oborot:
    print(f"Target not reached! You need {diff}lv. more.")
print(f"Earned money: {oborot}lv.")