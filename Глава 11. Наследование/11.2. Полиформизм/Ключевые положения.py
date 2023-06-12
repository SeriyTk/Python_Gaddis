import animals as anim
def main():
    mammal = anim.Mammal('обычное млекопитающее')
    mammal.show_species()
    mammal.make_sound()
    print()
    dog = anim.Dog()
    dog.show_species()
    dog.make_sound()
    print()
    cat = anim.Cat()
    cat.show_species()
    cat.make_sound()


if __name__ == '__main__': main()
