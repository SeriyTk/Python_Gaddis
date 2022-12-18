'''
В терминах программирования
цепочка символов, которая используется в качестве данных,
 называется символьной последователыюстью, или строковым значением, или просто строкой. Когда символьная после­
довательность появляется в рабочем коде программы, она называется строковым литералом.
'''
'''
В Python можно заключать строковые литералы в одинарные кавычки ( ') либо двойные
кавычки(").
'''
def doube_quotes():
    print("Кейт Остен")
    print("123 Фул Серкл Драйв")
    print("Эшвиль, Северная Каролина 28899")
doube_quotes()
print()
'''
Если требуется, чтобы строковый литерал содержал одинарную кавычку (апостроф), то
можно заключить строковый литерал в двойные кавычки.
'''
def apostгophe():
    print("Из всех рассказов О'Генри")
    print("мнe больше нравится'Вождь краснокожих'.")
apostгophe()
print()
'''
Аналогичным образом строковый литерал, в котором внутри содержатся двойные кавычки,
можно заключить в одинарные кавычки
'''
def display_quote():
    print('Домашнее задание на завтра - прочитать"Гамлета".')
display_quote()
print()
'''
Python позволяет заключать строковые литералы в тройные кавычки (""" либо ' ' '). Строки,
которые заключены в тройные кавычки, внутри могут содержать одинарные и двойные кавычки.
'''
print("""Bмecтo рассказов О'Генри сегодня займусь "Гамлетом".""")
print()
'''
Тройные кавычки используются для заключения многострочных строковых данных, для
которых одинарные и двойные кавычки не могут применяться.
'''
print("""Oдин
Два
Три""")