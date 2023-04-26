def main():
    cities = ['Нью-Йорк', 'Бостон', 'Атланта', 'Даллас']
    with open('cities.txt', 'w') as outfile:
        for item in cities: outfile.write(f'{item}\n')

    if __name__ == '__main__': main()

def main():
    with open('cities.txt') as infile:
        cities = infile.readlines()
        for index in range(len(cities)): cities[index] = cities[index].rstrip()
    print(cities)

    if __name__ == '__main__': main()

def main():
    numbers = [i for i in range(1, 8)]
    with open('numberlist.txt', 'w') as outfile:
        for item in numbers: outfile.write(f'{str(item)}\n')

    if __name__ == '__main__': main()

def main():
    with open('numberlist.txt') as infile:
        numbers = infile.readlines()
        for index in range(len(numbers)): numbers[index] = int(numbers[index])
    print(numbers)

if __name__ == '__main__': main()