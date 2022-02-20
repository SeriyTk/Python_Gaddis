# for переменная in строковое_значение:
        # инструкция
        # инструкция
name = 'Вася'
for ch in name:
    print(ch)

def count_Ts(par):
    count = 0
    for ch in par:
        if ch == 'т' or ch == 'Т':
            count += 1
    return count

print(f'Буква т появляется {count_Ts(input("Введите предложение: "))} раз.')