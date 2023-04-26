def main():
    codes = {'А' : '%' , 'а' : '9' , 'Б' : '@' , 'б' : "#" }
    with open('file_1.txt') as in_file, open('file_2.txt', 'w') as out_file:
        line = in_file.readline()
        for i in line:
            for k, v in codes.items():
                if i == k: out_file.write(v)
    with open('file_2.txt') as in_file:
        line = in_file.readline()
        for j in line: print(j)

if __name__ == '__main__': main()
