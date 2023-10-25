first = int(input())
second = int(input())
magic = int(input())

counter = 0
flag = False

for a in range(first, second + 1):
    for b in range(first, second + 1):
        counter += 1
        if a + b == magic:
            print(f"Combination N:{counter} ({a} + {b} = {magic})")
            flag = True
            break
    if flag:
        break

if not flag:
    print(f"{counter} combinations - neither equals {magic}")