# -*- coding: utf-8 -*-


def main():
    x, y = map(int, input().split())
    # -1 * n +     m = x
    #  2 * n + 2 * m = y
    m, q1 = divmod(2 * x + y, 4)
    n, q2 = divmod(-2 * x + y, 4)

    if y < 0:
        print(-1)
        exit()

    if q1 == 0 and q2 == 0:
        if m >= 0 and n >= 0:
            print(m + n)
        else:
            print(-1)
    else:
        print(-1)


if __name__ == '__main__':
    main()
