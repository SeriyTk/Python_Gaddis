def Loud_and_agreeable():
    loud_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    agreeable_list = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
    enter = 'Привет! Меня зовут Джо. А как твое имя?'
    print(f'Количество гласных: {num_loud(loud_list, enter)}, количество согласных: {num_agreeable(agreeable_list, enter)}.')


def num_loud(loud_list, enter):
    total_loud = 0
    for i in enter:
        for j in loud_list:
            if i.lower() == j:
                total_loud += 1
    return total_loud

def num_agreeable(agreeable_list, enter):
    total_agreeable = 0
    for i in enter:
        for j in agreeable_list:
            if i.lower() == j:
                total_agreeable += 1
    return total_agreeable




Loud_and_agreeable()
