def file_write():
    with open('philosophers .txt', 'w') as outfile:
        outfile.write('Вася Пупкин \n')
        outfile.write('Вова Вовин \n')
        outfile.write('Гриша Гришин \n')

if __name__ == '__main__': file_write()