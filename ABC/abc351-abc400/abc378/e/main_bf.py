# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        for j in range(i, n):
            ans += sum(a[i : j + 1]) % m

    print(ans)


if __name__ == "__main__":
    main()
