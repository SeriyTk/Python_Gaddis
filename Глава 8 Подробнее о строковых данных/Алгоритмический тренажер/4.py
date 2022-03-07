mystring = 'раммаПРП'
i = 0
counter = 0
ch = mystring[i]
while ch.islower():
    counter += 1
    i += 1
    ch = mystring[i]

print(counter)