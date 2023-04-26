def main():
    with open('test.txt') as document_text:
        text_string = document_text.read().lower()
        frequency = {}
        for word in text_string:
            count = frequency.get(word, 0)
            frequency[word] = count + 1
        frequency_list = frequency.keys()

        for words in frequency_list: print(words, frequency[words])



if __name__ == '__main__': main()
