LITER = 5
HOURS = 8
JOB = 2000
AREA = 10
def Appraiser():
    area_painted_wall = float(input("Площадь поверхности окрашиваемой стены: "))
    paint_containers = (area_painted_wall //AREA)
    if area_painted_wall % AREA == 0: print(f'Kоличество требуемых емкостей краски {paint_containers}')
    elif area_painted_wall % AREA != 0: print(f'Kоличество требуемых емкостей краски {paint_containers + 1}')
    hours_worked = area_painted_wall / AREA * HOURS
    print(f'Количество затраченных рабочих часов {hours_worked}')
    paint_cost = float(input('Стоимость краски: '))
    if area_painted_wall % AREA == 0: print(f'Стоимость краски {paint_containers * paint_cost}')
    elif area_painted_wall % AREA != 0: print(f'Стоимость краски {(paint_containers + 1) * paint_cost}')
    cost_of_work = hours_worked * JOB
    print(f'Стоимость работы {cost_of_work:,.2f}')

if __name__ == '__main__': Appraiser()