def main():
    recurse_str(1, int(input('Количество строк: ')))
def recurse_str(start, end):
    if start <= end: print('*' * start) ; recurse_str(start + 1, end)


if __name__ == '__main__': main()