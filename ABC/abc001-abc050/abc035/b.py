# -*- coding: utf-8 -*-


def main():
    s = list(input())
    t = int(input())
    x_axis = 0
    y_axis = 0
    question_count = 0

    for si in s:
        if si == 'L':
            x_axis -= 1
        elif si == 'R':
            x_axis += 1
        elif si == 'U':
            y_axis += 1
        elif si == 'D':
            y_axis -= 1
        else:
            question_count += 1

    const = abs(x_axis) + abs(y_axis)

    if t == 1:
        print(const + question_count)
    else:
        diff = const - question_count

        if diff >= 0:
            print(diff)
        else:
            print(abs(diff) % 2)


if __name__ == '__main__':
    main()
