def in_file(par):
    user = set()
    for i in par:
        user.add(i.rstrip())
    return user


def File_analysis():
    with open(r'G:\text_1.txt', encoding='utf-8') as inp_text_1, open(r'G:\text_2.txt', encoding='utf-8') as inp_text_2:
        user_1 = in_file(inp_text_1)
        user_2 = in_file(inp_text_2)

    print(user_1.union(user_2))
    print(user_1.intersection(user_2))
    print(user_1.difference(user_2))
    print(user_2.difference(user_1))
    print(user_1.symmetric_difference(user_2))


File_analysis()
