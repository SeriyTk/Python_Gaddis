def write_names():
    name1 = input('Друг №1: ')
    name2 = input('Друг №2: ')
    name3 = input('Друг №3: ')
    with open('frends.txt', 'w') as myfile:
        myfile.write(name1 + '\n')
        myfile.write(name2 + '\n')
        myfile.write(name3 + '\n')
    print('Имeнa бьmи запи саны в friends.txt.')



if __name__ == '__main__': write_names()
