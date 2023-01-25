count_symbol = int(input('Enter count symbols: '))
name_symbol = str(input('Enter symbol: '))
if count_symbol < 0:
    count_symbol = - count_symbol
for i in range(count_symbol):
    print(name_symbol)
