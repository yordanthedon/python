text = input()
tsum = 0

for i in range(0, len(text)):
    if text[i] == "a":
        tsum += 1
    if text[i] == "e":
        tsum += 2
    if text[i] == "i":
        tsum += 3
    if text[i] == "o":
        tsum += 4
    if text[i] == "u":
        tsum += 5
print(tsum)