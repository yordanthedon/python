k = int(input())
l = int(input())
m = int(input())
n = int(input())

count = 0

for q in range(k, 9):
    if q % 2 != 0:
        continue
    for w in range(9, l - 1, -1):
        if w % 2 == 0:
            continue
        for e in range(m, 9):
            if e % 2 != 0:
                continue
            for r in range(9, n - 1, - 1):
                if count == 6:
                    quit()

                if r % 2 == 0:
                    continue

                number1 = str(q) + str(w)
                number2 = str(e) + str(r)
                if number1 == number2:
                    print("Cannot change the same player.")
                else:
                    print(f"{number1} - {number2}")
                    count += 1