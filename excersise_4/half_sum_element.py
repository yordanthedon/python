import sys

number = int(input())
total = 0
max_num = -sys.maxsize
for i in range(1, number +1):
    n = int(input())
    if n > max_num:
        max_num = n
    total += n
other_nums = total - max_num
if other_nums == max_num:
    print("Yes")
    print(f"Sum = {other_nums}")
else:
    print("No")
    diff = abs(other_nums - max_num)
    print(f"Diff = {diff}")