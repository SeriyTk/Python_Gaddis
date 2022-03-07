def Word_separator():
    string = "ОстановисьИПочувствуйЗапахРоз"
    output_string = string[0]

    for char in string[1:]:
        if char.isupper():
            output_string += " " + char.lower()
        else:
            output_string += char

    print(output_string)



Word_separator()
