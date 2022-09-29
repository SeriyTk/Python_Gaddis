'''Полиморфизм позволяет подклассам иметь методы с теми же именами, что и у методовв их надклассах.
Это дает программе возможность вызывать правильный метод в зависимости от типа объекта,
который используется для его вызова.'''
import animals as anim
mammal = anim.Mammal('Обычное млекопитающее')
mammal.show_species()
mammal.make_sound()

собака = anim.Dog()
собака.show_species()
собака.make_sound()

кот = anim.Cat()
кот.show_species()
кот.make_sound()