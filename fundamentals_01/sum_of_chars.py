numbers_of_char = int(input())
ascii_values = 0
for char in range(numbers_of_char):
    next_char = input()
    ascii_values += ord(next_char)
print(f"The sum equals: {ascii_values}")