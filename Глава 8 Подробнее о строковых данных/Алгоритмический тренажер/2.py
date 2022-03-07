mystring = "Это моя строка the"
total = 0
for i in mystring:
    if i.isspace():
        total += 1

print(total)
