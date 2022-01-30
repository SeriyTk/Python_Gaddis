def prime_numbers():
    for num in range(2, 101):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            print(f'Число {num} простое.')

prime_numbers()

