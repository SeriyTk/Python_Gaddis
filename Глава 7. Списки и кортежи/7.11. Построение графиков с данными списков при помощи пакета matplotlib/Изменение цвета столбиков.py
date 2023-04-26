import matplotlib.pyplot as plt

def main():
    left_edges = [i for i in range(0, 41, 10)]
    heights = [i for i in range(100, 501, 100)]
    bar_width = 5
    plt.bar(left_edges, heights, bar_width, color = ('r', 'g', 'b', 'm', 'k'))
    plt.show()

if __name__ == '__main__': main()