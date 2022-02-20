filename = input('Введите имя файла: ')
if filename.endswith('.txt'):
    print('Этo имя текстового файла.')
elif filename.endswith('.ру'):
    print('Этo имя исходного файла Python. ')
elif filename.endswith('.doc'):
    print('Этo им документа текстового редактора.')
else:
    print('Неизвестный тип файла. ')

string = 'Восемьдесят семь лет назад'
position = string.find('семь')
if position != -1:
    print('Cлoвo "семь"найдено в индексной позиции', position)
else:
    print ('Слово "семь" не найдено.')

string = 'Восемьдесят семь лет назад'
new_string = string.replace('лет', 'дней')
print(new_string)