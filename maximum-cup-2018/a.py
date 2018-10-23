# -*- coding: utf-8 -*-


def main():
    n = int(input())
    count = 0

    for i in range(n):
        ti, di, mi = map(int, input().split())

        if (ti + 10) <= di:
            count += mi

    print(count)


if __name__ == '__main__':
    main()
