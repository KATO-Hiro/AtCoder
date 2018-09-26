# -*- coding: utf-8 -*-


def main():
    a = [list(map(int, input().split())) for _ in range(4)]

    for i in range(4):
        for j in range(3):
            if a[i][j] == a[i][j + 1]:
                print('CONTINUE')
                exit()

    for x in range(4):
        for y in range(3):
            if a[y][x] == a[y + 1][x]:
                print('CONTINUE')
                exit()

    print('GAMEOVER')


if __name__ == '__main__':
    main()
