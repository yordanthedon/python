square_meters = float(input())
whole_yard = square_meters * 7.61
whole_yard_discount = whole_yard * 0.18
yard = whole_yard - whole_yard_discount
print(f"The final price is: {yard} lv."
      f"The discount is: {whole_yard_discount} lv.")
