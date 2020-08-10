# -*- coding: utf-8 -*-


def main():
    board = list()

    for i in range(4):
        board.append(input())

    for grids in reversed(board):
        print(''.join(map(str, list(reversed(grids)))))


if __name__ == '__main__':
    main()
