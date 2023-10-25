pens = int(input())
marks = int(input())
liter_p = int(input())
disc = int(input())
pen = 5.80
mark = 7.20
p = 1.20
price_pen = pens * pen
price_mark = marks * mark
price_p = liter_p * p
all_sup = price_pen + price_mark + price_p
disc_p = all_sup * 0.25
total = all_sup - disc_p
print(total)