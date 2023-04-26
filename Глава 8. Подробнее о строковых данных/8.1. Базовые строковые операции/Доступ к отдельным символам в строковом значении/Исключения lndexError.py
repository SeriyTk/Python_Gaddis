city = 'Бостон'
index = 0
try:
    while index < 7: print(city[index]); index += 1
except IndexError as err: err