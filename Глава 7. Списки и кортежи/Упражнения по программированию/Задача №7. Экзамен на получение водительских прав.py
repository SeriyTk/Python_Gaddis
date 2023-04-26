ROWS = 20
COLS = 2
def main():
    with open('right_answers.txt', 'w') as infile:
        write_list(ROWS, COLS, infile)

def write_list(R, C, infile):
    list_answers = [[input(': ') for c in range(COLS)] for r in range(ROWS)]
    for r in range(R):
        for c in range(C): infile.write(f'{list_answers[r][c]}\n')


    if __name__ == '__main__': main()
def main():
    with open('student_solution.txt', 'w') as infile:
        list_solution = [[input('Ответ: ') for c in range(COLS)] for r in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS): infile.write(f'{list_solution[r][c]}\n')


if __name__ == '__main__': main()