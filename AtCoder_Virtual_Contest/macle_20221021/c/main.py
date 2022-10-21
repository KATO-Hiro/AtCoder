# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))[::-1]
    c = list(map(int, input().split()))[::-1]
    ans = list()

    for i in range(n + m + 1):
        if i  > m:
            continue
    
        ratio = c[i] // a[0]
        ans.append(ratio)

        for j in range(n + 1):
            c[i + j] -= ratio * a[j]

    print(*ans[::-1])


if __name__ == "__main__":
    main()
