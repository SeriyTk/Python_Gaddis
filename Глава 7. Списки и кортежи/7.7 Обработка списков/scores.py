def get_scores():
    test_scores = []
    while True:
        if input('Ввести оценку? д =да, все остальное= нет: ') != 'д':
            break
        else:
            test_scores.append(float(input('Bвeдитe оценку: ')))

    return test_scores

def get_total(scor):
    total = 0
    for num in scor: total += num
    return total
