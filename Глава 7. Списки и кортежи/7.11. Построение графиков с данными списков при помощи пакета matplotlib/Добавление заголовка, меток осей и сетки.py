import matplotlib.pyplot as plt

def main():
    х_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]
    plt.plot(х_coords, y_coords)
    plt.title('График')
    plt.xlabel("Ось х")
    plt.ylabel("Ось y")
    plt.grid(True)
    plt.show()


if __name__ == '__main__': main()