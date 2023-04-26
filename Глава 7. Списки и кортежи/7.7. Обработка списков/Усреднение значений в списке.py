def main():
    numbers = [i for i in range(2, 11, 2)]
    print(numbers)
    total = 0
    for value in numbers: total += value
    average = total / len(numbers)
    print(f'Cpeднee значение элементов составляет {average}.')

if __name__ == '__main__': main()