# -*- coding: utf-8 -*-


def main():
    a = [list(map(int, input().split())) for _ in range(4)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    for x in range(4):
        for y in range(4):
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if 0 <= new_x <= 3 and 0 <= new_y <= 3:
                    if a[x][y] == a[new_x][new_y]:
                        print('CONTINUE')
                        exit()

    print('GAMEOVER')


if __name__ == '__main__':
    main()
