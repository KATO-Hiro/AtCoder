# -*- coding: utf-8 -*-


def main():
    p = [list(input()) for _ in range(10)]
    count = 0

    for j in range(10):
        is_exist = False

        for i in range(10):
            if p[i][j] == 'o':
                is_exist = True
                break

        if is_exist:
            count += 1

    if count == 10:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
