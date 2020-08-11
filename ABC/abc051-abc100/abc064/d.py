# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    count = 0
    new_left = 0
    new_right = 0

    # See:
    # https://www.youtube.com/watch?v=5FOTOiV5p0U
    for si in s:
        if si == '(':
            count += 1
        else:
            count -= 1

            if count == -1:
                count = 0
                new_left += 1

    new_right = count

    print('(' * new_left + s + ')' * new_right)


if __name__ == '__main__':
    main()
