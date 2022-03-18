dct = {'Вася': 555 - 11 - 1, "Федя": 555 - 11 - 2}
if "Вася" in dct:
    del dct["Вася"]
    print(dct)
else:
    print("Не найден.")
