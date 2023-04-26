def main():
    with open('test_scores.csv') as csv_file:
        lines = csv_file.readlines()
    for line in lines:
        tokens = line.split(',')
        total = 0
        for token in tokens: total += float(token)
        average = total / len(tokens)
        print(f'Cpeдний балл: {average} ')

if __name__ == '__main__': main()
