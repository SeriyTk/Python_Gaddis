def Morse_code_converter(par):
    list_Simbole = [' ', ',', '.', '?','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G',
                            'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    list_Kode = ['пробел','—..—','.-.-.-','..--..','-----','.----','..---','...--','....-','.....','-....','—...','---..','----.','.-','-...','-.-.','-..','.','..-.','—.',
                            '....','..','.---','-.-','.-..','--','-.','---','.--.','—.-','.-.','...','-','..-','...-','.--','-..-','-.-','--..']
    for n in range(len(list_Simbole)):
        if par == list_Simbole[n]:
            return list_Kode[n]


print(Morse_code_converter(input('Введите символ: ')))
