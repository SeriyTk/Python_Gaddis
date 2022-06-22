def main():
    with open('index.html', 'w') as out_file:
        name = input('Введите свое имя: ')
        print('Опишите себя: ')
        descr = ""
        while True:
            enter = input()
            if enter: descr += enter +' '+'\n'
            else: break
        print(f'''
<html>
<head>
</head>
<body>
    <center><h1>{name}</h1></center>
    <hr />
    {descr}
    <hr />
</body>
</html>
''', file=out_file)


main()
