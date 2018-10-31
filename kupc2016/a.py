# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())
    count = 0

    for i in range(n):
        ti = int(input())

        if a <= ti < b:
            pass
        else:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
