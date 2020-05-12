# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    a, b, c, k = map(int, input().split())
    ans = 0
    ans += min(a, k)

    k -= a

    if k > 0:
        k -= b

    if k > 0:
        ans -= k

    print(ans)


if __name__ == '__main__':
    main()
