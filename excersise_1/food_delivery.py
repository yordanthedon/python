chiken_menus = int(input())
fish_menus = int(input())
veg_menus = int(input())
chiken_price = 10.35
fish_price = 12.40
veg_price = 8.15
delivery = 2.50
c_m = chiken_menus * chiken_price
f_m = fish_menus * fish_price
v_m = veg_menus * veg_price
total_m = c_m + f_m +v_m
dessert = total_m * 0.2
total_delivery = total_m + dessert + delivery
print(total_delivery)
