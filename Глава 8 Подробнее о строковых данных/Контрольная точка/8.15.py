while True:
    enter = input('Желаете повторить программу или выйти П\В: ')
    if enter.lower() == 'п' and enter.upper() == 'П':
        continue
    elif enter.lower() == 'в' and enter.upper() == 'В':
        break