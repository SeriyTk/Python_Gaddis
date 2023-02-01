def multiple_args():
    print('Cyммa чисел 12 и 45 равняется')
    show_sum(12,45)

def show_sum(num1, num2): print(num1 + num2)

if __name__ == '__main__': multiple_args()
print()
def string_args():
    print('Bawe имя в обратн ом порядке')
    reverse_name(input('Введите свое имя: '), input('Введите свою фамилию: '))

def reverse_name(first, last): print(last, first)

if __name__ == '__main__': string_args()