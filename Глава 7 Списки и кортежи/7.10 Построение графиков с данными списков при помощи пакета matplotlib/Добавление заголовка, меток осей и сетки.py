import matplotlib.pyplot as plt


def line_graph():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]
    plt.plot(x_coords, y_coords)
    plt.title('Это образец')
    plt.xlabel('Это ось x')
    plt.ylabel('Это ось y')
    plt.grid(True)
    plt.show()


line_graph()
