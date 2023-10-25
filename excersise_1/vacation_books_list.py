pages_book = int(input())
pages_hour = int(input())
days_book = int(input())
one_book = pages_book // pages_hour
per_day = one_book // days_book
print(per_day)