import random

num1 = random.randint(1, 300)
num2 = random.randint(1, 300)

print(f'''
    {num1}
+  {num2}
''')
enter = int(input('Ответ: '))
if enter == num1 + num2: print('Все правильно.')
else: print(f'Ответ не правильный, правильный ответ {num2 + num1}')