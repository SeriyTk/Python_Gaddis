import scores


def main():
    scor = scores.get_scores()
    total = scores.get_total(scor)
    total -= min(scor)
    average = total / (len(scor) - 1)
    print('Средняя оценка с учетом отброшенной, самой низкой оценкой составляет: ',average)


main()
