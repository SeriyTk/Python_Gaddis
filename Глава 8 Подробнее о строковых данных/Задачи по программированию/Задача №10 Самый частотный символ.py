def Most_frequent_symbol():
    string = 'cccc8923jbbdkcc'
    chars = {}
    for i in string:
        chars.update({string.count(i): i})
    print((max(chars.items())[1]))

Most_frequent_symbol()