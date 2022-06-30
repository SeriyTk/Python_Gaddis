def main():
    print(f'Числа в списке: {get_values()}')

def get_values():
    values = []
    while True:
        again = input('д =да, все остальное= нет: ')
        if again != 'д': break
        else: values.append(int(input('Bвeдитe число: ')))
        print()
    return values


main()
