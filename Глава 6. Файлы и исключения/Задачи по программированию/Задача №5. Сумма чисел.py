def main():
    '''
        with open('numbers.txt', 'w') as out_file:
        for number in range(100): print(number + 1, file=out_file)
    '''
    total_sum = 0
    for number in open('numbers.txt'): total_sum += int(number)
    print(total_sum)



main()
