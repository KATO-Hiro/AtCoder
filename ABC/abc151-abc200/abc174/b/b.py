# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, d = map(int, input().split())
    d2 = d ** 2
    ans = 0

    for i in range(n):
        xi, yi = map(int, input().split())

        if ((xi ** 2) + (yi ** 2)) <= d2:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
