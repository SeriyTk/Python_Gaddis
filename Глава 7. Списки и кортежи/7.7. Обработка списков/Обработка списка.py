def main():
    scores = get_scores()
    total = get_total(scores)
    lowest = min(scores)
    total -= lowest
    average = total / (len(scores) - 1)
    print(f'Cpeдняя оценка с учетом отброшенной самой низкой оценки: {average}')

def get_scores():
    test_scores = []
    while True:
        print('Жeлaeтe добавить оценку?')
        again = input('enter =да, все остальное= нет: ')
        if again != '': break
        else:
            value = float(input('Bвeдитe оценку: '))
            test_scores.append(value)
            print()
    return test_scores
def get_total(value_list):
    total = 0
    for num in value_list: total += num
    return total

if __name__ == '__main__': main()