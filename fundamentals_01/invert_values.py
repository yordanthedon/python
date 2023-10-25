list_numbers = input().split()
opposite_numbers = []
for i in range(len(list_numbers)):
    opposite_number = -int(list_numbers[i])
    opposite_numbers.append(opposite_number)
print(opposite_numbers)