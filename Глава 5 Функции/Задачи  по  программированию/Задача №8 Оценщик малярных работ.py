START = 10
ST_OIL = 5
ST_TIME = 8
BID = 2000
def Painting_appraiser():
    num_oil, working_hours, paint_cost,working_cost, total_cost = job_evaluation()
    print(f'Количество требующихся емкостей краски {num_oil}.')
    print(f'Количество требующихся рабочих часов {working_hours}.')
    print(f'Стоимость краски {paint_cost}.')
    print(f'Стоимость работы {working_cost:,.2f}.')
    print(f'Общая стоимость малярных работ {total_cost:,.2f}.')

def job_evaluation():
    surface_area = float(input("Площадь окращиваемой поверхности: "))
    price_oil = float(input('Цена банки краски: '))
    num_oil = (surface_area + START - 1) // START  #количество требующихся емкостей краски
    working_hours = surface_area / START * ST_TIME # количество требующихся рабочих часов
    paint_cost = num_oil * price_oil # стоимость краски
    working_cost = working_hours * BID # стоимость работы
    total_cost= paint_cost + working_cost #общая стоимость малярных работ
    return num_oil, working_hours, paint_cost,working_cost, total_cost
Painting_appraiser()