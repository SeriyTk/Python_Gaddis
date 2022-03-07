def Sentence_Corrector():
    s = "привет! меня зовут джо. а как твое имя?".split()
    s[0] = s[0].title()
    for i in range(len(s) - 1):
        if s[i][-1] in '!?.':
            s[i + 1] = s[i + 1].title()
    print(' '.join(s))


Sentence_Corrector()
