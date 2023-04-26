def main():
    with open('pushkin-metel.txt') as text_file:
        text = text_file.read().lower().split()
        print(set(text))

if __name__ == '__main__': main()
