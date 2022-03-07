def str_split(par):
    world_split = par.split()
    return world_split


print(str_split('Один два три четыре'))


date_string = '01/12/2018'
date_list = date_string.split('/')
print(f'День:   {date_list[0]}.')
print(f'Месяц: {date_list[1]}.')
print(f'Год:   {date_list[2]}.')
