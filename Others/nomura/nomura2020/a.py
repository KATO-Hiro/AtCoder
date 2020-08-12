# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    h1, m1, h2, m2, k = map(int, input().split())

    h = (h2 - h1) * 60
    m = m2 - m1
    ans = h + m - k
    print(ans)


if __name__ == '__main__':
    main()
