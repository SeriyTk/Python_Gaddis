mystring = '36547asd254'
i = 0
counter = 0
ch = mystring[i]
while ch.isdigit():
    counter += 1
    i += 1
    ch = mystring[i]

print(counter)