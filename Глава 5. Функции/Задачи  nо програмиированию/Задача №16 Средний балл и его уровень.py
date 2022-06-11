def main():
    print('Введите 5 оценок.')
    total_eval = 0
    num_eval = 0
    for i in range(5):
        eval = int(input(f'Введите оценку №{i + 1}: '))
        print('Оценка\tУровень')
        print('---------------------')
        print(f'{eval}   \t\t      {determine_grade(eval)}')
        total_eval += eval
        num_eval += 1
    print('----------------------------------------------------------------')
    print(f'Средний бал {calc_average(total_eval, num_eval):.2f}')

def calc_average(total_eval, num_eval): return total_eval / num_eval
def determine_grade(eval):
    if eval >= 90: return 'A'
    elif 80 <= eval < 90: return 'B'
    elif 70 <= eval < 80: return 'C'
    elif 60 <= eval < 70: return 'D'
    else: return 'F'
main()
