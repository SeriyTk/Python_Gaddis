def temperature():
    MAX_TEMP = 102.5
    while True:
        temperature = input('Введите темрературу в градусах Цельсия: ')
        if temperature == 'stop': break
        else:
            if float(temperature) > MAX_TEMP:
                print('Teмпepaтypa слишком высокая.')
                print('Убавьте нагрев и подождите 5 минут. ')
                print('Затем снимите показание температуры cнoвa и введите полученное значение.')
            elif float(temperature) <= MAX_TEMP: print ('Температура приемлемая.')


a = 0
while a < 10: print(a, end=' '); a += 1
print()
y = int(input(': '))
x = y // 2
while x > 1:
    if y % x == 0: print (y, 'hasfactor', x); break
    x -= 1
else: print (y,'is prime')