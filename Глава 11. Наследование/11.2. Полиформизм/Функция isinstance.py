import animals as anim
def main():
    mammal = anim.Mammal('обычное животное')
    dog = anim.Dog()
    cat = anim.Cat()
    print('Вот несколько животных и звуки, которые они издают.')
    print('------------------------------------------------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
def show_mammal_info(creat):
    creat.show_species()
    creat.make_sound()

    if __name__ == '__main__': main()
def main():
    mammal = anim.Mammal('обычное животное')
    dog = anim.Dog()
    cat = anim.Cat()
    print('Вот несколько животных и звуки, которые они издают.')
    print('------------------------------------------------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    print()
    show_mammal_info('Я - последовательность символов')
def show_mammal_info(creat):
    if isinstance(creat, anim.Mammal):
        creat.show_species()
        creat.make_sound()
    else: print('Этo не млекопитающее!')

if __name__ == '__main__': main()
