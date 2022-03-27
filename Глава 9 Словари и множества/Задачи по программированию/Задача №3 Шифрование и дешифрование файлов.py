def out_dictionary_creation():
    codes = {}
    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alfavit_RU_lower = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower()
    for letter in alfavit_RU:
        codes[letter] = input(f'Кодировка буквы {letter}: ')

    for letter in alfavit_RU_lower:
        codes[letter] = input(f'Кодировка буквы {letter}: ')
    with open(r'G:\codes.txt', 'w') as f_codes:
        for key, value in codes.items():
            print(key, file=f_codes)
            print(value, file=f_codes)
    print('Файл создан.')

def in_dictionary_creation():
    codes = {}
    with open(r'G:\codes.txt') as f_codes:
        key = f_codes.readline()
        while key != '':
            value = f_codes.readline()
            codes[key.rstrip()] = value.rstrip()
            key = f_codes.readline()
    print(codes)
def File_encryption_and_decryption():
    in_dictionary_creation()


File_encryption_and_decryption()
