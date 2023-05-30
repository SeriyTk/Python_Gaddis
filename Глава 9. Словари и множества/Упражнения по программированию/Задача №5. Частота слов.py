from collections import Counter
def main():
    with open('test.txt') as document_text:
        text_string = document_text.read().lower().split()
        word_list = []
        for word in text_string:
            clear_word = ''
            for letter in word:
                if letter.isalpha(): clear_word += letter

            word_list.append(clear_word)

    print(Counter(word_list))
if __name__ == '__main__': main()
