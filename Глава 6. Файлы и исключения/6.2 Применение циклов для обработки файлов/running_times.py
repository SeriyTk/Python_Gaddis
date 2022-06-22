def save_running_times():
    with open('video_times.txt', 'w') as video_file:
        print('Введите длительность каждого видеоклипа.')
        for count in range(int(input('Cкoлькo видеоклипов в проекте?: '))):
            print(input(f'Видеоклип №{count + 1}: '), file=video_file)

        print('Времена сохранены в video_ times. txt. ')

def read_running_times():
    total = 0
    count = 0
    print('Длительности всех видеоклипов:')
    for line in open('video_times.txt'): count += 1; print(f'Видеоклип №{count}: {float(line)}', sep=''); total += float(line)
    print(f'Oбщaя дпительность составляет {total} секунд.')