class Car:
    def __init__(self, year_mod, make, speed = 0):
        self.__year_mod = year_mod
        self.__make = make
        self.__speed = speed

    def set_year_mod(self, year_mod): self.__year_mod = year_mod
    def set_make(self, make): self.__make = make
    def set_speed(self, speed): self.__speed = speed

    def get_year_mod(self): return self.__year_mod
    def get_make(self): return self.__make
    def get_speed(self): return  self.__speed

    def accelerate(self, speed): self.__speed += speed
    def stop(self, speed): self.__speed -= speed

