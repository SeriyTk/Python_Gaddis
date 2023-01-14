def temperature():
    MAX_TEMP = 102.5
    while True:
        temperature = float(input("Bвeдитe температуру вещества в градусах Цельсия: "))
        if temperature > MAX_TEMP:
            print(f'''
Teмпepaтypa слишком высокая.
Убавьте нагрев и подождите 5 минут. Затем снимите показание температуры
cнoвa и введите полученное значение.
''')
        elif temperature <= MAX_TEMP: print('Teмпepaтypa приемлемая.Проверьте ее снова через 15 минут.'); break


temperature()