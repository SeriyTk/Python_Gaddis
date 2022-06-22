def main():
    with open('number_list.txt', 'w') as out_file:
        for number in range(100): print(f'{number + 1}', file=out_file)


main()
