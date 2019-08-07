# -*- coding: utf-8 -*-


def decimal_to_bin(n: int, m: int = 2) -> int:
    ans = ''

    while n >= m:
        p, q = divmod(n, m)
        n = p
        ans += str(q)

        if n < m:
            ans += str(p)

    return int(ans[::-1])


def main():
    n, x = map(int, input().split())

    for i in range(2, 10 + 1):
        if decimal_to_bin(n, i) == x:
            print(i)
            exit()


if __name__ == '__main__':
    main()
