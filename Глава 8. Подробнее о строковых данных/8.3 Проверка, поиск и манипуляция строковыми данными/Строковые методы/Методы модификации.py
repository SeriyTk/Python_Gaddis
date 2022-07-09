letters = 'ABC'
print(letters, letters.lower())
print()
letters = 'abc'
print(letters, letters.upper())
print()
while True:
    again = input('д =да, все остальное= нет: ')
    if not again: print("Конец."); break
    else:
        if again.lower() == 'д': print('Привет!')