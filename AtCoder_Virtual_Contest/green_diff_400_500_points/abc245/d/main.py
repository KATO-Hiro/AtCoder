# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))[::-1]
    c = list(map(int, input().split()))[::-1]
    ans = list()

    # 下の桁から筆算
    for i in range(m + 1):
        r = c[i] // a[0]
        ans.append(r)

        for j in range(i, i + n + 1):
            c[j] -= r * a[j - i]

    print(*ans[::-1])


if __name__ == "__main__":
    main()
