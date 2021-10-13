# -*- coding: utf-8 -*-


def count_divisor(n):
    ans = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans.add(i)
            ans.add(n // i)

    return len(ans)


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())
    x_count = count_divisor(x)
    y_count = count_divisor(y)

    if x_count > y_count:
        print('X')
    elif x_count < y_count:
        print('Y')
    else:
        print('Z')


if __name__ == "__main__":
    main()
