import matplotlib.pyplot as plt

def main():
    х_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]
    plt.plot(х_coords, y_coords)

    plt.title('График')

    plt.xlabel("Ось х")
    plt.ylabel("Ось y")

    plt.xlim(xmin = -1, xmax = 10)
    plt.ylim(ymin = -1, ymax = 6)
    plt.grid(True)
    plt.show()


    if __name__ == '__main__': main()

def main():
    х_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]
    plt.plot(х_coords, y_coords)

    plt.title('Пpoдaжи с разбивкой по годам')

    plt.xlabel("Год")
    plt.ylabel("Объем продаж")

    plt.xticks([0, 1, 2, 3, 4], ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 1, 2, 3, 4, 5], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    plt.grid(True)
    plt.show()


if __name__ == '__main__': main()