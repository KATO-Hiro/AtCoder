# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    x = int(input())
    ans = 0

    p, q = divmod(x, 500)
    ans += 1000 * p
    ans += q // 5 * 5

    print(ans)


if __name__ == '__main__':
    main()
