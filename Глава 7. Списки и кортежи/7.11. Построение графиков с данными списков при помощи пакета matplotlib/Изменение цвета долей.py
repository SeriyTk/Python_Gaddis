import matplotlib.pyplot as plt

def main():
    sales = [100, 400, 300, 600]
    slice_labels = ['I квартал', 'II квартал', 'III квартал', 'IV квартал']
    plt.pie(sales, labels = slice_labels, colors=('r', 'g', 'b', 'm', 'k'))
    plt.title('Пpoдaжи с разбивкой по кварталам')
    plt.show()

if __name__ == '__main__': main()