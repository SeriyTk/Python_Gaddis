def Calculating_the_factorial_of_a_number(number):
    factorial = 1
    for i in range(number):
        factorial *= i + 1
    return factorial


print(Calculating_the_factorial_of_a_number(4))
