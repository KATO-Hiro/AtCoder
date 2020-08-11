# -*- coding: utf-8 -*-


def main():
    q, h, s, d = list(map(int, input().split()))
    n = int(input())

    # See:
    # https://www.youtube.com/watch?v=9OiB8ot3a0w
    x = min(4 * q, h * 2, s)
    print(min(n * x, d * (n // 2) + n % 2 * x))


if __name__ == '__main__':
    main()
