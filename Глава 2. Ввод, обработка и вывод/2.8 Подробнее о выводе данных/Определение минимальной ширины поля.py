print(format(12345.6789, '12,.2f'))
def columns():
    num1 = 127.899
    num2 = 3465.148
    num3 = 3.776
    num4 = 264.821
    num5 = 88.081
    num6 = 799.999


    print(format(num1, '8.2f'))
    print(format(num2, '7.2f'))
    print(format(num3, '10.2f'))
    print(format(num4, '8.2f'))
    print(format(num5, '9.2f'))
    print(format(num6, '9.2f'))

columns()

reply = '''
Greetings...
Hello %(name)s!
Your age is %(age)s
'''
values = { 'name' : 'Bob' , 'age' : 40}
print(reply % values)
print( '{:10} = {: 10}'.format('spam', 123.4567))