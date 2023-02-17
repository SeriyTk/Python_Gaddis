def main():
    total = 0
    quantity = 0
    try:
        with open('numbers.txt') as infile:
            for line in infile: total += float(line); quantity += 1
    except IOError as err: print(err)
    except ValueError as err: print(err)
    except ZeroDivisionError as err: print(err)
    finally: print(total / quantity)



if __name__ == '__main__': main()