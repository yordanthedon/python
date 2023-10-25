width = int(input())
length = int(input())

volume = width * length
sum_piece = 0
input_line = input()

while input_line != "STOP":
    piece = int(input_line)
    sum_piece += piece

    if sum_piece >= volume:
        break

    input_line = input()

diff = abs(sum_piece - volume)

if sum_piece > volume:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")