# -*- coding: utf-8 -*-


def main():
    n, y = map(int, input().split())

    for i in range(n + 1):
        for j in range(n - i + 1):
            if 9 * i + 4 * j == y // 1000 - n:
                print(i, j, n - (i + j))
                exit()

    print(-1, -1, -1)


if __name__ == '__main__':
    main()
