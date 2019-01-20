# -*- coding: utf-8 -*-


def main():
    q, h, s, d = map(int, input().split())
    n = int(input())
    ans = 0

    if n % 2 == 0:
        ans = min(8 * q, 4 * h, 2 * s, d) * (n // 2)
    else:
        ans = min(8 * q, 4 * h, 2 * s, d) * (n // 2)
        ans += min(4 * q, 2 * h, s)

    print(int(ans))


if __name__ == '__main__':
    main()
