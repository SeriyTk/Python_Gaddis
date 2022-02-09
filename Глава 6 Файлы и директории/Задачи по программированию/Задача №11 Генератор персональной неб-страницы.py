def write_descr():
    text = ""
    print('Введите описание: ')
    while True:
        x = input()
        if x:
            text += x + " "
        else:
            break
    return text

def web_page_generator():
    with open(r'G:\index.html', 'w') as f:
        print(f'''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="windows-1251">
    <title></title>
</head>
<body>
    <center>
    <h1>{input('Введите свое имя: ')}</h1>
    </center>
    <p>{write_descr()}</p>
</body>
</html>
        ''', file=f)


web_page_generator()
