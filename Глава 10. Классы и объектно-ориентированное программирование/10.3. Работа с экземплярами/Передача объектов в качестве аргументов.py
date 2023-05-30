import coin
def main():
    my_coin = coin.Coin()
    print(my_coin)
    flip(my_coin)
    print(my_coin)
def flip(obj): obj.toss()

if __name__ == '__main__': main()
