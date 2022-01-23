import math


def area_circle(radius):
    return math.pi * radius ** 2


def circumference(radius):
    return 2 * math.pi * radius


def rectangle(a, b):
    area_rectangle(a, b)
    perimeter_rectangle(a, b)


def area_rectangle(a, b):
    return a * b


def perimeter_rectangle(a, b):
    return (a + b) * 2
