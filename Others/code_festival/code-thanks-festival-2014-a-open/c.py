# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    s = list(map(int, input().split()))
    ans = 0

    for si in s:
        ans += p[si - 1]

    print(ans)


if __name__ == '__main__':
    main()
