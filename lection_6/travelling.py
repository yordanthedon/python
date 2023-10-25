data=input()
money_dest=0
money_dest_needed=0
while data!='End':
    if money_dest_needed==0:
        destination=data
    if money_dest_needed==0:
        money_dest_needed=float(input())
    if money_dest==0:
        money=float(input())
    else:
        money=float(data)
    money_dest+=money
    if money_dest>=money_dest_needed:
        print(f'Going to {destination}!')
        money_dest=0
        money_dest_needed=0
    data=input()