# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    dices = [int(input()) for _ in range(n)]
    dirs = [int(input()) for _ in range(m)]
    print(dices, dirs)
    i = 0

    for index, _dir in enumerate(dirs, 1):
        i += _dir
        print(i)
        # print(dices[i])


if __name__ == '__main__':
    main()
