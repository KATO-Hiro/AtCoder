# -*- coding: utf-8 -*-


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(bin(x)[2:])[::-1]
    ans = 0

    for index, bi in enumerate(b):
        ans += a[index] * int(bi)

    print(ans)


if __name__ == '__main__':
    main()
