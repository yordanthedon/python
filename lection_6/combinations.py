number = int(input())
combinations = 0
for a in range(0, number + 1):
    for b in range(0, number + 1):
        for c in range(0, number + 1):
            if a + b + c == number:
                combinations += 1
print(combinations)

