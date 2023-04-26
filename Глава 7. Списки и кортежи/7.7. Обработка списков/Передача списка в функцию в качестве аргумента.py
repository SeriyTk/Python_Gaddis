def main():
    numbers = [i for i in range(2, 11, 2)]
    print(f'Cyммa составляет {get_total(numbers)}. ')

def get_total(num_list):
    total = 0
    for i in num_list: total += i
    return total


if __name__ == '__main__': main()