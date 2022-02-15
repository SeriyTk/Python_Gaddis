def get_scores():
    scores = []
    num_scores = 0
    while True:
        scores.append(float(input(f'Получить оценку №{num_scores + 1}: ')))
        num_scores += 1
        print('Ввести еще одну оценку?')
        answer = input('Если да - введите д: ')
        if  answer != "д":
            print("Оценки в список занесены.")
            break
    return scores


def get_total_scores(par):
    total_scores = 0
    for score in par:
        total_scores += score
    return total_scores



def get_min_score(par):
    return min(par)



def get_adjusted_amount(par1, par2):
    par1 -= par2
    return par1



def drop_lowest_score(par):
    return get_adjusted_amount(get_total_scores(par),get_min_score(par)) / (len(par)-1)






print(f'Средняя оценка за вычетом отброшеной {drop_lowest_score(get_scores())}.')


