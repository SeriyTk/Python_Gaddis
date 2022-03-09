def Youth_jargon():
    string = 'ПРОСПАЛ ПОЧТИ ВСЮ НОЧЬ'.split(' ')
    ki = 'КИ'
    for i in string:
        print(i[1:] + i[0] + ki, end=" ")


Youth_jargon()
