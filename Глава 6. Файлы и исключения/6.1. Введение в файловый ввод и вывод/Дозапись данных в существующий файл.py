def write_newline():
    with open('philosophers .txt', 'a') as myfile:
        line1 = myfile.write('Юра \n')
        line2 = myfile.write('Саша \n')
        line3 = myfile.write('Витя \n')


if __name__ == '__main__': write_newline()
