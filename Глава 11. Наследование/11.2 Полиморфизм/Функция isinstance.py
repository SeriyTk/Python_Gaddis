import animals as anim

def main():
    животное = anim.Mammal('Обычное животное')
    собака = anim.Dog()
    кот = anim.Cat()

    anim.show_mammal_info(животное)
    anim.show_mammal_info(собака)
    anim.show_mammal_info(кот)
    anim.show_mammal_info('Я - последовательность символов')

if __name__ == '__main__': main()