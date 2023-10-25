kg_veg = float(input())
kg_fruit = float(input())
t_veg = int(input())
t_fruit = int(input())
veg_price = kg_veg * t_veg
fruit_price = kg_fruit * t_fruit
total = (veg_price + fruit_price) / 1.94
print(f'{total: .2f}')