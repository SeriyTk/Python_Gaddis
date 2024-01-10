BASE_SIZE = 8
def rectangular_pattern():
    for r in range(BASE_SIZE):
        for c in range(r + 1): print('*', end='')
        print()


if __name__ == '__main__': rectangular_pattern = rectangular_pattern()
print()
NUM_STEPS = 6
def stair_step_pattern():
    for r in range(NUM_STEPS):
        for c in range(r): print(' ', end='')
        print('#')

if __name__ == '__main__': stair_step_pattern = stair_step_pattern()
