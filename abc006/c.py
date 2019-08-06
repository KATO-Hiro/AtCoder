# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    diff = 4 * n - m

    if diff < 0:
        print(-1, -1, -1)
        exit()

    x = 0
    y = diff

    while y >= 2:
        x += 1
        y -= 2
        z = n - (x + y)

        if z >= 0:
            print(x, y, z)
            exit()

    print(-1, -1, -1)


if __name__ == '__main__':
    main()
