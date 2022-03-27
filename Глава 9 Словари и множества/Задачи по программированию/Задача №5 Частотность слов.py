def Word_frequency():
    frequency = {}
    with open(r'G:\pushkin-metel.txt', encoding="utf-8") as input_file:
        text = input_file.read().lower()[:300]
    list_znak = ['\n',',',';','.','!']
    for j in list_znak:
        text = text.replace(j,'')
    dct = text.split()
    for word in dct:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
    frequency_list = frequency.keys()

    for words in frequency_list:
        frequency[words]

    print(frequency)

        



Word_frequency()
