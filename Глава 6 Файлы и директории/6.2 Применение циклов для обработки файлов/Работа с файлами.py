def save_running_times():
    with open(r'G:\video_times.txt', 'w') as video_file:
        num_videos = int(input('Количество видеоклипов в проэкте: '))
        for count in range(1, num_videos + 1):
            print(input(f'Длительность видеоклипа №{count}: '), file=video_file)

    print('Времена сохранены в video_times.txt.')

def read_running_times():
    with open(r'G:\video_times.txt') as video_file:
        total_times = 0
        count = 1
        for time in video_file:
            print(f'Длина видеоклипа №{count} равна {float(time)}.')
            count += 1
            total_times += float(time)

    print(f'Общая длительность всех видеоклипов {total_times} сек.')

read_running_times()