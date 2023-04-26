def get_login(first, last, idnum):
    set1 = first[0 : 3]
    set2 = last[0 : 3]
    set3 = idnum[-3 : ]
    return set1 + set2 + set3
