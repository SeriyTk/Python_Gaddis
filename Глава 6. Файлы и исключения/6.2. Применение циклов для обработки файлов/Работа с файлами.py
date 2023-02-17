def save_running_times():
    num_videos = int(input('Cкoлькo видео клипов в проекте? '))
    with open('video_times.txt', 'w') as video_file:
        print('Введите длительность каждого видео клипа.')
        for count in range(num_videos):
            run_time = float(input(f'Bидeoклип No {count + 1}: '))
            video_file.write(f'{run_time}\n')
    print('Времена сохранены в video_ times. txt. ')
if __name__ == '__main__': save_running_times()
print()
def read_running_times():
    with open('video_times.txt') as video_file:
        total = 0.0
        count = 0
        print('Длительности все видеоклипов: ')
        for line in video_file:
            run_time = float(line)
            count += 1
            print(f'Видеоклип № {count}: {run_time}', sep=' ')
            total += run_time

    print(f'Oбщaя длительность составляет {total} секунд.')

if __name__ == '__main__': read_running_times()