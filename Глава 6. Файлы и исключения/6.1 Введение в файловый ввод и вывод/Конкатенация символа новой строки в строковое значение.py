def main():
    print('Введите имена трех друзей.')
    with open('friends.txt', 'w') as myfile:
        for i in range(3): print(input(f'Друг №{i + 1}: '), file=myfile)

    print('Имeнa были записаны в friends.txt. ')

main()
