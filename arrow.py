import time
import os


arrow_length = 20
arrow_brick = '.'
arrow_freq = 1


def rotating_arrow(length: int, brick: chr, freq: float):
    # arrow east
    os.system('cls')

    for line in range(0, (length//2 - 1)):
        print()

    for line in range(0, length):
        if line < (length // 2):
            print(' ' * (int)(length * 1.5) + brick * (line))
        elif line == (length // 2):
            print(' ' * (length) + brick * (length))
        else:
            print(' ' * (int)(length * 1.5) + brick * (length - line))

    time.sleep(freq)
    # -----------------------------------------------

    # arrow south
    os.system('cls')

    for line in range(0, (length - 1)):
        print()

    for line in range(0, length):
        if line < (length / 2):
            print(' ' * length + brick)
        else:
            print(' ' * (length//2 + 1) + ' ' * (line - (length//2)), end='')
            print((brick) * (2*length-(2*line)-1))

    time.sleep(freq)

    # -----------------------------------------------

    # arrow west
    os.system('cls')

    for line in range(0, (length//2 - 1)):
        print()

    for line in range(0, length):
        if line < (length // 2):
            print(' ' * (length//2 - line) + brick * (line))
        elif line == (length // 2):
            print(brick * (length))
        else:
            print(' ' * (line - length//2) + brick * (length - line))

    time.sleep(freq)
    # -----------------------------------------------

    # arrow north
    os.system('cls')

    for line in range(0, length):
        if line < (length / 2):
            print(' ' * (length - line) + ' ' * (line - (length//2)), end='')
            print((brick) * ((2*line)+1))

        else:
            print(' ' * length + brick)

    time.sleep(freq)


# accelerating rotaion
for n in range(20, 1, -1):
    rotating_arrow(arrow_length, arrow_brick, (n/50))

# decelerating rotaion
for n in range(1, 20, 1):
    rotating_arrow(arrow_length, arrow_brick, (n/50))
