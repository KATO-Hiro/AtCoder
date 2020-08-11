# -*- coding: utf-8 -*-


def main():
    m, n, large_n = map(int, input().split())
    ans = large_n
    new = 0

    while large_n >= m:
        new = (large_n // m) * n
        ans += new
        large_n = new + large_n % m

    print(ans)


if __name__ == '__main__':
    main()
