import random as rdm


def main():
    while True:
        random_number = rdm.randint(1, 101)
        a_guess = int(input("Угадайте число: "))
        if random_number < a_guess: print('Слишком много, попробуйте еще раз')
        elif random_number > a_guess: print('Слишком мало, попробуйте еще раз')
        else: print('Ура!'); break

main()
