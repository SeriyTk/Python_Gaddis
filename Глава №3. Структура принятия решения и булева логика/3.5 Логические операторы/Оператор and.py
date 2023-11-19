def main():
    temperature = int(input('Введите температуру: '))
    minutes = int(input('Введите минуты: '))
    if temperature < 0 and minutes > 100: print('Teмпepaтypa находится в опасной зоне.')


if __name__ == '__main__': main()
