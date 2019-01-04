# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(h):
        for k in range(w):
            if board[i][k] == '#':
                count = 0

                for m in range(4):
                    x = i + dx[m]
                    y = k + dy[m]

                    if 0 <= x < h and 0 <= y < w and board[x][y] == '#':
                        count += 1

                if count == 0:
                    print('No')
                    exit()

    print('Yes')


if __name__ == '__main__':
    main()
