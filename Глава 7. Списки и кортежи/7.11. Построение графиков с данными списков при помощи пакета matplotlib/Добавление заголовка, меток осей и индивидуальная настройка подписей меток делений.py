import matplotlib.pyplot as plt

def main():
    left_edges = [i for i in range(0, 41, 10)]
    heights = [i for i in range(100, 501, 100)]
    bar_width = 5
    plt.bar(left_edges, heights, bar_width, color = ('r', 'g', 'b', 'm', 'k'))
    plt.title('Пpoдaжи с разбивкой по годам')
    plt.xlabel('Год')
    plt.ylabel('Объем продаж')
    plt.xticks([5, 15, 25, 35, 45], ['2016', '2017', '2018', '2018', '2020'])
    plt.yticks([0, 100, 200, 300, 400, 500], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    plt.show()

if __name__ == '__main__': main()